"""
intent_routing_service.py

Purpose
-------
Determine which specialist agents should
process a user's request.

Responsibilities
----------------
- Normalize requests
- Detect business intent
- Extract customer identifiers
- Route requests to specialist agents

Author
------
Credit Risk Research Agent
"""

import re

from typing import List

from src.config.intent_rules import (
    CUSTOMER_ID_PATTERN,
    POLICY_LANGUAGE,
    POLICY_SUBJECTS,
    CUSTOMER_INTENT
)


class IntentRoutingService:
    """
    Determines which specialist agents
    should process a request.
    """

    POLICY_AGENT = "policy"

    CUSTOMER_AGENT = "customer"

    def identify_agents(
        self,
        request: str
    ) -> List[str]:
        """
        Determine which specialist
        agents should process a request.
        """

        request = self._normalize_request(
            request
        )

        customer = False

        policy = False

        customer_id = (
            self.extract_customer_id(
                request
            )
        )

        # -----------------------------------------
        # Customer Intent
        # -----------------------------------------

        if customer_id:

            customer = True

        elif self._contains_customer_intent(
            request
        ):

            customer = True

        # -----------------------------------------
        # Policy Intent
        # -----------------------------------------

        if self._contains_policy_intent(
            request
        ):

            policy = True

        # -----------------------------------------
        # Routing Decision
        # -----------------------------------------

        if policy and customer:

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

    # ---------------------------------------------------------
    # Customer Identifier
    # ---------------------------------------------------------

    def extract_customer_id(
        self,
        request: str
    ) -> str | None:
        """
        Extract customer identifier from
        a natural language request.
        """

        match = re.search(
            CUSTOMER_ID_PATTERN,
            request.upper()
        )

        if match:

            return match.group()

        return None

    # ---------------------------------------------------------
    # Helper Methods
    # ---------------------------------------------------------

    def _normalize_request(
        self,
        request: str
    ) -> str:

        return request.lower().strip()

    def _contains_customer_intent(
        self,
        request: str
    ) -> bool:
        """
        Determine whether the request
        represents customer analysis.
        """

        return any(

            keyword in request

            for keyword

            in CUSTOMER_INTENT

        )

    def _contains_policy_intent(
        self,
        request: str
    ) -> bool:
        """
        Determine whether the request
        represents policy interpretation.
        """

        has_language = any(
        word in request
        for word in POLICY_LANGUAGE
        )

        has_subject = any(
            subject in request
            for subject in POLICY_SUBJECTS
        )

        return has_language or has_subject