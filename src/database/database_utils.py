"""
database_utils.py

Purpose:
Provides reusable SQLite database utilities
for creating tables, inserting records,
executing queries, and managing connections.

Author:
Credit Risk Research Agent
"""

import sqlite3

from pathlib import Path
from typing import List
from typing import Tuple
from typing import Optional


class DatabaseManager:
    """
    Generic SQLite database manager.

    This class provides reusable helper methods
    for creating tables, inserting records,
    querying data, and committing transactions.
    """

    def __init__(
        self,
        database_path: str
    ):
        """
        Initialize database connection.

        Parameters
        ----------
        database_path : str
            Path to SQLite database.
        """

        self.database_path = Path(
            database_path
        )

        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            self.database_path
        )

        self.connection.row_factory = (
            sqlite3.Row
        )

        self.cursor = (
            self.connection.cursor()
        )

        print(
            f"Connected to database:\n"
            f"{self.database_path}"
        )

    # --------------------------------------------------
    # Table Creation
    # --------------------------------------------------

    def create_tables(
        self,
        table_queries: List[str]
    ):
        """
        Execute CREATE TABLE statements.
        """

        for query in table_queries:

            self.cursor.execute(
                query
            )

        self.connection.commit()

        print(
            f"Created {len(table_queries)} table(s)"
        )

    # --------------------------------------------------
    # Index Creation
    # --------------------------------------------------

    def create_indexes(
        self,
        index_queries: List[str]
    ):
        """
        Execute CREATE INDEX statements.
        """

        for query in index_queries:

            self.cursor.execute(
                query
            )

        self.connection.commit()

        print(
            f"Created {len(index_queries)} index(es)"
        )

    # --------------------------------------------------
    # Execute Single Query
    # --------------------------------------------------

    def execute(
        self,
        query: str,
        parameters: tuple = ()
    ):
        """
        Execute a single SQL statement.
        """

        self.cursor.execute(
            query,
            parameters
        )

        self.connection.commit()

    # --------------------------------------------------
    # Bulk Insert
    # --------------------------------------------------

    def executemany(
        self,
        query: str,
        records: List[Tuple]
    ):
        """
        Execute bulk insert operations.
        """

        self.cursor.executemany(
            query,
            records
        )

        self.connection.commit()

    # --------------------------------------------------
    # Fetch All
    # --------------------------------------------------

    def fetch_all(
        self,
        query: str,
        parameters: tuple = ()
    ):
        """
        Execute query and
        return all rows.
        """

        self.cursor.execute(
            query,
            parameters
        )

        return self.cursor.fetchall()

    # --------------------------------------------------
    # Fetch One
    # --------------------------------------------------

    def fetch_one(
        self,
        query: str,
        parameters: tuple = ()
    ):
        """
        Execute query and
        return one row.
        """

        self.cursor.execute(
            query,
            parameters
        )

        return self.cursor.fetchone()

    # --------------------------------------------------
    # Count Records
    # --------------------------------------------------

    def get_row_count(
        self,
        table_name: str
    ) -> int:
        """
        Return number of rows
        in a table.
        """

        self.cursor.execute(
            f"""
            SELECT COUNT(*)
            FROM {table_name}
            """
        )

        return self.cursor.fetchone()[0]

    # --------------------------------------------------
    # Table Exists
    # --------------------------------------------------

    def table_exists(
        self,
        table_name: str
    ) -> bool:
        """
        Check whether a table exists.
        """

        self.cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name=?
            """,
            (table_name,)
        )

        return (
            self.cursor.fetchone()
            is not None
        )

    # --------------------------------------------------
    # Commit
    # --------------------------------------------------

    def commit(self):
        """
        Commit transaction.
        """

        self.connection.commit()

    # --------------------------------------------------
    # Close Connection
    # --------------------------------------------------

    def close(self):
        """
        Close database connection.
        """

        self.connection.close()

        print(
            "Database connection closed."
        )


# --------------------------------------------------
# Local Testing
# --------------------------------------------------

if __name__ == "__main__":

    db = DatabaseManager(
        database_path=(
            "data/customers/customer.db"
        )
    )

    print(
        "\nDatabase Connected Successfully"
    )

    db.close()
