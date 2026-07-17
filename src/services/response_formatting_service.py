"""
response_formatting_service.py

Purpose
-------
Format Coordinator Agent responses into
a presentation-friendly response while
preserving the underlying agent outputs.

Responsibilities
----------------
- Format Policy Agent responses
- Format Customer Agent responses
- Format composite responses
- Preserve standardized response contracts

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
    Formats Coordinator responses for
    presentation.
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

            return self._format_policy_response(
                response
            )

        if agents == ["customer"]:

            return self._format_customer_response(
                response
            )

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
        response
    ):

        return {

            "success": True,

            "response_type": "policy",

            "answer": (

                response["responses"]["policy"]

            )

        }

    # ---------------------------------------------------------
    # Customer
    # ---------------------------------------------------------

    def _format_customer_response(
        self,
        response
    ):

        return {

            "success": True,

            "response_type": "customer",

            "customer": (

                response["responses"]["customer"]

            )

        }

    # ---------------------------------------------------------
    # Policy + Customer
    # ---------------------------------------------------------

    def _format_policy_customer_response(
        self,
        response
    ):

        return {

            "success": True,

            "response_type": "policy_customer",

            "policy": (

                response["responses"]["policy"]

            ),

            "customer": (

                response["responses"]["customer"]

            )

        }
