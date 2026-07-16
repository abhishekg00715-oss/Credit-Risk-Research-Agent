"""
intent_routing_service.py

Purpose:
Determine which specialist agents should
process a user's request.

The service performs lightweight,
deterministic intent detection using
keyword-based matching.

Responsibilities:
- Normalize incoming requests
- Identify required business capabilities
- Return one or more target agents

Future Enhancements:
- Configurable routing rules
- NLP / LLM intent classification
- Confidence scoring

Author:
Credit Risk Research Agent
"""

from typing import List


class IntentRoutingService:
    """
    Determines which specialist agents
    should process a request.
    """

    POLICY_AGENT = "policy"
    CUSTOMER_AGENT = "customer"

    def __init__(self):
        """
        Initialize routing keywords.
        """

        self._policy_keywords = {

            "policy",
            "guideline",
            "eligibility",
            "criteria",
            "minimum score",
            "ltv",
            "dti",
            "credit policy",
            "rule",
            "document",
            "manual"
        }

        self._customer_keywords = {

            "customer",
            "customer id",
            "credit score",
            "bureau",
            "utilization",
            "income",
            "loan",
            "profile",
            "assessment",
            "risk summary"
        }

    def identify_agents(
        self,
        request: str
    ) -> List[str]:
        """
        Determine which agents should
        process the request.
        """

        normalized_request = self._normalize_request(
            request
        )

        agents = []

        if self._is_policy_request(
            normalized_request
        ):

            agents.append(
                self.POLICY_AGENT
            )

        if self._is_customer_request(
            normalized_request
        ):

            agents.append(
                self.CUSTOMER_AGENT
            )

        return agents

    def _normalize_request(
        self,
        request: str
    ) -> str:
        """
        Normalize user request.
        """

        return request.lower().strip()

    def _is_policy_request(
        self,
        request: str
    ) -> bool:
        """
        Determine whether the request
        requires the Policy Agent.
        """

        return any(

            keyword in request

            for keyword in self._policy_keywords

        )

    def _is_customer_request(
        self,
        request: str
    ) -> bool:
        """
        Determine whether the request
        requires the Customer Agent.
        """

        return any(

            keyword in request

            for keyword in self._customer_keywords

        )
