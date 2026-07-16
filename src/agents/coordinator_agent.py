"""
coordinator_agent.py

Purpose:
Central orchestration layer responsible
for routing user requests to the
appropriate agent.

Current Capabilities:
Policy Agent
Customer Risk Agent

Future:
Portfolio Agent
Recommendation Agent

Author:
Credit Risk Research Agent
"""

from src.agents.policy_agent import PolicyAgent

from src.agents.customer_agent import CustomerAgent

from src.services.intent_routing_service import (
    IntentRoutingService
)


class CoordinatorAgent:
    """
    Central orchestration agent.
    """

    def __init__(self):
        """
        Initialize routing service
        and specialist agents.
        """

        self.routing_service = (
            IntentRoutingService()
        )

        self._initialize_agents()

    def _initialize_agents(self):
        """
        Register available agents.
        """

        self._agents = {
            "policy": {
                "instance": PolicyAgent(),
                "method": "answer_question"
            },
            "customer": {
                "instance": CustomerAgent(),
                "method": "retrieve_customer_profile"
            }
        }

    def route_query(
        self,
        query: str
    ) -> str:
        """
        Determine which agent should
        process the query.

        """
         agent_names = (
            self.routing_service
            .identify_agents(query)
        )

        if not agent_names:

            return self._build_error_response(
                "Unable to determine the appropriate agent."
            )

        responses = {}

        for agent_name in agent_names:

            responses[agent_name] = (
                self._invoke_agent(
                    agent_name,
                    query
                )
            )

        return {

            "success": True,

            "agents_invoked": agent_names,

            "responses": responses

        }
        
        

     def _invoke_agent(
        self,
        agent_name,
        query
    ):
        """
        Execute the selected agent.
        """
            agent = self._agents[agent_name]
            handler = getattr(agent["instance"], agent["method"])
            return handler(query)
    

    def _build_error_response(
        self,
        message
    ):
        """
        Build standardized error
        response.
        """

        return {

            "success": False,

            "message": message,

            "agents_invoked": [],

            "responses": {}

        }

    

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
