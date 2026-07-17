"""
response_formatting_service.py

Purpose
-------
Transform Coordinator Agent responses into a
presentation-friendly model.

Responsibilities
----------------
- Standardize presentation structure
- Organize responses into semantic sections
- Preserve business responses
- Remain UI independent

Future Enhancements
-------------------
- Portfolio formatting
- Recommendation formatting
- Explainability formatting

Author
------
Credit Risk Research Agent
"""

from typing import Any, Dict


class ResponseFormattingService:
    """
    Builds a presentation model for the UI.
    """

    def format_response(
        self,
        response: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Format Coordinator response.
        """

        if not response["success"]:
            return response

        agents = response["agents_invoked"]

        if agents == ["policy"]:
            return self._format_policy_response(response)

        if agents == ["customer"]:
            return self._format_customer_response(response)

        if (
            "policy" in agents
            and
            "customer" in agents
        ):
            return self._format_policy_customer_response(
                response
            )

        return response

    # ---------------------------------------------------------
    # Policy
    # ---------------------------------------------------------

    def _format_policy_response(
        self,
        response: Dict[str, Any]
    ) -> Dict[str, Any]:

        return {

            "success": True,

            "response_type": "policy",

            "title": "Policy Response",

            "sections": [

                {
                    "heading": "Answer",
                    "type": "text",
                    "content": response["responses"]["policy"]
                }

            ]

        }

    # ---------------------------------------------------------
    # Customer
    # ---------------------------------------------------------

    def _format_customer_response(
        self,
        response: Dict[str, Any]
    ) -> Dict[str, Any]:

        return {

            "success": True,

            "response_type": "customer",

            "title": "Customer Assessment",

            "sections": [

                {
                    "heading": "Assessment",
                    "type": "customer",
                    "content": response["responses"]["customer"]
                }

            ]

        }

    # ---------------------------------------------------------
    # Policy + Customer
    # ---------------------------------------------------------

    def _format_policy_customer_response(
        self,
        response: Dict[str, Any]
    ) -> Dict[str, Any]:

        return {

            "success": True,

            "response_type": "policy_customer",

            "title": "Customer Policy Assessment",

            "sections": [

                {
                    "heading": "Applicable Policy",
                    "type": "text",
                    "content": response["responses"]["policy"]
                },

                {
                    "heading": "Customer Assessment",
                    "type": "customer",
                    "content": response["responses"]["customer"]
                }

            ]

        }
