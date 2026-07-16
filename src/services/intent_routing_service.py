class IntentRoutingService:
    """
    Determines which specialist agents should
    process a user request.
    """

    def identify_agents(
        self,
        user_request: str
    ) -> list[str]:
        """Return a list of agent identifiers."""

    def _normalize_request(
        self,
        user_request: str
    ) -> str:
        """Normalize input for matching."""

    def _is_customer_request(
        self,
        request: str
    ) -> bool:
        """Detect customer-related intent."""

    def _is_policy_request(
        self,
        request: str
    ) -> bool:
        """Detect policy-related intent."""
