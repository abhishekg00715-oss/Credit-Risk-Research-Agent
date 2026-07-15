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

import os
import sys
from typing import Any, Dict

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

from repository.customer_repository import CustomerRepository
from services.customer_assessment_service import (
    CustomerAssessmentService
)
from services.customer_summary_service import (
    CustomerSummaryService
)



class CustomerAgent:
    """
    Customer Agent.

    Provides a clean interface between the Coordinator Agent
    and the Customer Repository.
    """

    def __init__(
        self,
        repository: CustomerRepository | None = None,
        assessment_service: CustomerAssessmentService | None = None,
        summary_service: CustomerSummaryService | None = None
    ) -> None:
    
        self.repository = (
            repository
            if repository
            else CustomerRepository()
        )
    
        self.assessment_service = (
            assessment_service
            if assessment_service
            else CustomerAssessmentService()
        )
    
        self.summary_service = (
            summary_service
            if summary_service
            else CustomerSummaryService()
        )

# ------------------------------------------------------------------
# Validation Helpers
# ------------------------------------------------------------------

    def _validate_customer_id(
        self,
        customer_id: str
    ) -> bool:
        """
        Validate the supplied customer identifier.
    
        Parameters
        ----------
        customer_id : str
    
        Returns
        -------
        bool
            True if the customer identifier is valid.
        """
    
        return (
            isinstance(customer_id, str)
            and bool(customer_id.strip())
        )

# ------------------------------------------------------------------
# Response Helpers
# ------------------------------------------------------------------

    def _build_success_response(
        self,
        customer_profile: Dict[str, Any],
        assessment: Dict[str, Any] | None = None,
        risk_summary: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:
        """
        Build a standardized success response.
        """
    
        return ({
            "success": True,
            "message": "Customer profile retrieved successfully.",
            "customer_profile": customer_profile,
            "assessment": assessment,
            "risk_summary": risk_summary,
        })

    
    # ---------------------------------------------------------
    #  Error Response
    # ---------------------------------------------------------
    
    
    def _build_error_response(
        self,
        message: str
    ) -> Dict[str, Any]:
        """
        Build a standardized error response.
        """
    
        return ({
            "success": False,
            "message": message,
            "customer_profile": None,
            "assessment": None,
            "risk_summary": None,
        })
        
        
    # ---------------------------------------------------------
    # Customer Lookup
    # ---------------------------------------------------------

    def retrieve_customer_profile(
        self,
        customer_id: str
    ) -> Dict[str, Any]:
        """
        Retrieve a complete customer profile.
        """
        
        if not self._validate_customer_id(customer_id):
    
            return self._build_error_response(
                "Customer ID cannot be empty."
            )
    
        customer_profile = (
            self.repository.get_customer_profile(customer_id)
        )
    
        if customer_profile["customer"] is None:
    
            return self._build_error_response(
                f"Customer '{customer_id}' was not found."
            )
        assessment = self.assessment_service.assess_customer(
            customer_profile,
        )

        risk_summary = self.summary_service.generate_customer_summary(
            customer_profile,
            assessment
        )
        return self._build_success_response(
            customer_profile=customer_profile,
            assessment=assessment,
            risk_summary=risk_summary
        )

    # ---------------------------------------------------------
    # Self Test
    # ---------------------------------------------------------

# ------------------------------------------------------------------
# Test Harness
# ------------------------------------------------------------------

if __name__ == "__main__":

    agent = CustomerAgent()

    response = agent.retrieve_customer_profile(
        "CUST000001"
    )

    from pprint import pprint

    pprint(response)
