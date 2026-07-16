"""
intent_routing_service.py

Purpose
-------
Determine which specialist agents should
process a user's request.

Responsibilities
----------------
- Normalize requests
- Detect customer intent
- Detect policy intent
- Extract customer identifiers
- Return target agents
"""

import re

from typing import List


class IntentRoutingService:

    POLICY_AGENT = "policy"
    CUSTOMER_AGENT = "customer"

    CUSTOMER_ID_PATTERN = r"\bCUST\d{6}\b"

    def __init__(self):

        self._policy_anchors = {

            "policy",
            "guideline",
            "guidelines",
            "criteria",
            "eligibility",
            "rule",
            "rules",
            "underwriting",
            "approval",
            "decline",
            "minimum",
            "maximum",
            "required",
            "threshold",
            "credit policy",
            "premium credit card",
            "manual",
            "document"

        }

        self._customer_anchors = {

            "customer",
            "customer id",
            "customer profile",
            "profile",
            "assessment",
            "risk summary",
            "bureau"

        }

    def identify_agents(
        self,
        request: str
    ) -> List[str]:

        request = self._normalize_request(request)

        customer = False
        policy = False

        if self._contains_customer_identifier(request):
            customer = True

        elif self._contains_customer_anchor(request):
            customer = True

        if self._contains_policy_anchor(request):
            policy = True

        if customer and policy:
            return [
                self.POLICY_AGENT,
                self.CUSTOMER_AGENT
            ]

        if policy:
            return [
                self.POLICY_AGENT
            ]

        if customer:
            return [
                self.CUSTOMER_AGENT
            ]

        return []

    def extract_customer_id(
        self,
        request: str
    ) -> str | None:
        """
        Extract customer identifier
        from a natural language request.
        """

        match = re.search(
            self.CUSTOMER_ID_PATTERN,
            request.upper()
        )

        if match:
            return match.group()

        return None

    def _normalize_request(
        self,
        request: str
    ) -> str:

        return request.lower().strip()

    def _contains_customer_identifier(
        self,
        request: str
    ) -> bool:

        return (
            self.extract_customer_id(request)
            is not None
        )

    def _contains_customer_anchor(
        self,
        request: str
    ) -> bool:

        return any(

            keyword in request

            for keyword

            in self._customer_anchors

        )

    def _contains_policy_anchor(
        self,
        request: str
    ) -> bool:

        return any(

            keyword in request

            for keyword

            in self._policy_anchors

        )