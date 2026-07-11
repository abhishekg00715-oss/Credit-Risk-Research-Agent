"""
customer_repository.py

Purpose:
--------
Provides a repository layer for accessing customer-related
information stored in the SQLite customer database.

This class abstracts all database interactions from higher
application layers such as the Customer Agent.

Responsibilities:
-----------------
- Establish database connections
- Execute SQL queries
- Retrieve customer-related data
- Return query results as dictionaries

Out of Scope:
-------------
- Business rules
- Risk calculations
- Customer assessment
- Recommendation generation
- Data transformation beyond database retrieval

Author:
-------
Credit Risk Research Agent
"""

from pathlib import Path
import sqlite3
import logging

from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)
 # Default database location
    DEFAULT_DATABASE_PATH = (
        Path(__file__).resolve().parent.parent
        / "database"
        / "customer_risk.db"
    )

class CustomerRepository:
    """
    Repository responsible for retrieving customer information
    from the SQLite database.

    The repository exposes simple methods for retrieving
    customer-related records while hiding SQL implementation
    details from consuming components.
    """

    def __init__(self, database_path: Optional[str] = None) -> None:
        """
        Initialize the repository.

        Parameters
        ----------
        database_path : str, optional
            Custom path to the SQLite database.
            If not provided, the default project database is used.
        """

        self.database_path = (
            Path(database_path)
            if database_path
            else self.DEFAULT_DATABASE_PATH
        )

    # ------------------------------------------------------------------
    # Database Helper Methods
    # ------------------------------------------------------------------

    def _get_connection(self) -> sqlite3.Connection:
        """
        Create and return a SQLite database connection.

        Returns
        -------
        sqlite3.Connection
            SQLite connection object configured to return rows
            as dictionaries.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        return connection

    def _fetch_one(
        self,
        query: str,
        parameters: tuple = ()
    ) -> Optional[Dict[str, Any]]:
        """
        Execute a query expected to return a single record.

        Parameters
        ----------
        query : str
            SQL query.

        parameters : tuple
            Query parameters.

        Returns
        -------
        dict | None
            Dictionary representation of the row if found,
            otherwise None.
        """

        with self._get_connection() as connection:

            cursor = connection.execute(query, parameters)
            row = cursor.fetchone()

        return dict(row) if row else None

    def _fetch_all(
        self,
        query: str,
        parameters: tuple = ()
    ) -> List[Dict[str, Any]]:
        """
        Execute a query expected to return multiple rows.

        Parameters
        ----------
        query : str
            SQL query.

        parameters : tuple
            Query parameters.

        Returns
        -------
        List[dict]
            List of dictionaries.
        """

        with self._get_connection() as connection:

            cursor = connection.execute(query, parameters)
            rows = cursor.fetchall()

        return [dict(row) for row in rows]

    # ------------------------------------------------------------------
    # Customer Master
    # ------------------------------------------------------------------

    def get_customer(
        self,
        customer_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve customer master information.

        Parameters
        ----------
        customer_id : str

        Returns
        -------
        dict | None
        """

        query = """
            SELECT *
            FROM customer_master
            WHERE customer_id = ?
        """

        return self._fetch_one(query, (customer_id,))

    # ------------------------------------------------------------------
    # Credit Bureau
    # ------------------------------------------------------------------

    def get_credit_bureau(
        self,
        customer_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve customer bureau information.
        """

        query = """
            SELECT *
            FROM credit_bureau
            WHERE customer_id = ?
        """

        return self._fetch_one(query, (customer_id,))

    # ------------------------------------------------------------------
    # Credit Cards
    # ------------------------------------------------------------------

    def get_credit_cards(
        self,
        customer_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieve all credit cards for a customer.
        """

        query = """
            SELECT *
            FROM credit_card_accounts
            WHERE customer_id = ?
            ORDER BY card_id
        """

        return self._fetch_all(query, (customer_id,))

    # ------------------------------------------------------------------
    # Loan Accounts
    # ------------------------------------------------------------------

    def get_loans(
        self,
        customer_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieve all loans for a customer.
        """

        query = """
            SELECT *
            FROM loan_accounts
            WHERE customer_id = ?
            ORDER BY loan_id
        """

        return self._fetch_all(query, (customer_id,))

    # ------------------------------------------------------------------
    # Transactions
    # ------------------------------------------------------------------

    def get_transactions(
        self,
        customer_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieve customer transactions.
        """

        query = """
            SELECT *
            FROM transactions
            WHERE customer_id = ?
            ORDER BY transaction_date DESC
        """

        return self._fetch_all(query, (customer_id,))

    # ------------------------------------------------------------------
    # Digital Behaviour
    # ------------------------------------------------------------------

    def get_digital_behavior(
        self,
        customer_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieve customer digital behaviour.
        """

        query = """
            SELECT *
            FROM digital_behavior
            WHERE customer_id = ?
            ORDER BY login_timestamp DESC
        """

        return self._fetch_all(query, (customer_id,))

    # ------------------------------------------------------------------
    # Composite Customer Profile
    # ------------------------------------------------------------------

    def get_customer_profile(
        self,
        customer_id: str
    ) -> Dict[str, Any]:
        """
        Retrieve the complete customer profile.

        This is a convenience method that aggregates all
        customer-related information into a single object.

        No business rules or calculations are performed.
        """

        return {

            "customer": self.get_customer(customer_id),

            "credit_bureau": self.get_credit_bureau(customer_id),

            "credit_cards": self.get_credit_cards(customer_id),

            "loans": self.get_loans(customer_id),

            "transactions": self.get_transactions(customer_id),

            "digital_behavior": self.get_digital_behavior(customer_id)
        }
