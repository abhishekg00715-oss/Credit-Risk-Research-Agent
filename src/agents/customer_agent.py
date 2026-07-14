"""
customer_agent.py

Purpose
-------
Customer Agent responsible for orchestrating retrieval of
customer information from the Customer Repository.

Responsibilities
----------------
- Receive customer lookup requests
- Validate input
- Retrieve customer profile
- Return standardized response objects

Out of Scope
------------
- SQL queries
- Risk calculations
- Credit assessment
- Recommendations
- Portfolio analysis

Author
------
Credit Risk Research Agent
"""

from typing import Any, Dict

from repository.customer_repository import CustomerRepository


class CustomerAgent:
    """
    Customer Agent.

    Provides a clean interface between the Coordinator Agent
    and the Customer Repository.
    """

    def __init__(
        self,
        repository: CustomerRepository | None = None
    ) -> None:
        """
        Initialize Customer Agent.

        Parameters
        ----------
        repository : CustomerRepository, optional

            Repository instance.

            If omitted, a default repository will be created.
        """

        self.repository = (
            repository
            if repository
            else CustomerRepository()
        )

    # ---------------------------------------------------------
    # Customer Lookup
    # ---------------------------------------------------------

    def get_customer_profile(
        self,
        customer_id: str
    ) -> Dict[str, Any]:
        """
        Retrieve complete customer profile.

        Parameters
        ----------
        customer_id : str

        Returns
        -------
        dict

            Standardized customer response.
        """

        if not customer_id:

            return {

                "success": False,

                "message": "Customer ID cannot be empty.",

                "customer_profile": None
            }

        profile = self.repository.get_customer_profile(
            customer_id
        )

        if profile["customer"] is None:

            return {

                "success": False,

                "message": f"Customer '{customer_id}' was not found.",

                "customer_profile": None
            }

        return {

            "success": True,

            "message": "Customer profile retrieved successfully.",

            "customer_profile": profile
        }

    # ---------------------------------------------------------
    # Self Test
    # ---------------------------------------------------------

if __name__ == "__main__":

    agent = CustomerAgent()

    response = agent.get_customer_profile(
        "CUST000001"
    )

    print(response["message"])

    if response["success"]:

        print(response["customer_profile"]["customer"])
