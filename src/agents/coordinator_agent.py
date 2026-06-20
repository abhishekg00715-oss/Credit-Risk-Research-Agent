"""
coordinator_agent.py

Purpose:
Central orchestration layer responsible
for routing user requests to the
appropriate agent.

Current MVP:
Routes all queries to Policy Agent.

Future:
Policy Agent
Customer Risk Agent
Portfolio Agent
Recommendation Agent

Author:
Credit Risk Research Agent
"""

from src.agents.policy_agent import PolicyAgent


class CoordinatorAgent:
    """
    Central orchestration agent.
    """

    def __init__(self):
        """
        Initialize available agents.
        """

        self.policy_agent = PolicyAgent()

    def route_query(
        self,
        query: str
    ) -> str:
        """
        Determine which agent should
        process the query.

        Current MVP:
        Route all requests to Policy Agent.
        """

        print(
            "\nCoordinator Agent:"
            " Routing query to Policy Agent..."
        )

        return self.policy_agent.answer_question(
            query
        )

    def process_query(
        self,
        query: str
    ) -> str:
        """
        Main entry point for all user queries.
        """

        if not query.strip():

            return (
                "Please provide a valid query."
            )

        response = self.route_query(
            query
        )

        return response


if __name__ == "__main__":

    coordinator = CoordinatorAgent()

    query = (
        "What is the minimum credit "
        "score required for a premium "
        "credit card?"
    )

    response = coordinator.process_query(
        query
    )

    print("\nResponse")
    print("=" * 80)
    print(response)
