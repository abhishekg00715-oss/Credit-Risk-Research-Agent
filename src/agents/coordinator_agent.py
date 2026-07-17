"""
coordinator_agent.py

Purpose
-------
Central orchestration layer responsible
for routing user requests to the
appropriate specialist agent.

Current Capabilities
--------------------
- Policy Agent
- Customer Agent

Future Capabilities
-------------------
- Portfolio Agent
- Recommendation Agent
- Explainability Agent

Responsibilities
----------------
- Determine required specialist agents
- Delegate requests to the appropriate agent(s)
- Aggregate responses
- Return a standardized orchestration response

Author
------
Credit Risk Research Agent
"""
import time
from typing import Any, Dict

from src.agents.customer_agent import CustomerAgent
from src.agents.policy_agent import PolicyAgent
from src.services.intent_routing_service import (
    IntentRoutingService
)
from src.services.response_formatting_service import (
    ResponseFormattingService
)
from src.logging.query_logger import QueryLogger
from src.logging.agent_execution_logger import (
    AgentExecutionLogger
)


class CoordinatorAgent:
    """
    Central orchestration agent.
    """

    QUERY_INPUT = "query"
    CUSTOMER_ID_INPUT = "customer_id"

    def __init__(self) -> None:
        """
        Initialize routing service
        and specialist agents.
        """

        self.routing_service = (
            IntentRoutingService()
        )

        self._register_agents()
        self.response_formatter = (
            ResponseFormattingService()
        )
        self.query_logger = QueryLogger()
        self.execution_logger = (
            AgentExecutionLogger()
        )

    # ---------------------------------------------------------
    # Agent Registration
    # ---------------------------------------------------------

    def _register_agents(self) -> None:
        """
        Register all available
        specialist agents.
        """

        self._agents = {

            "policy": {

                "instance": PolicyAgent(),

                "method": "answer_question",

                "input_type": self.QUERY_INPUT

            },

            "customer": {

                "instance": CustomerAgent(),

                "method": "retrieve_customer_profile",

                "input_type": self.CUSTOMER_ID_INPUT

            }

        }

    # ---------------------------------------------------------
    # Routing
    # ---------------------------------------------------------

    def route_query(
        self,
        query: str,
        correlation_id: str
    ) -> Dict[str, Any]:
        """
        Route the request to one or
        more specialist agents.
        """

        agent_names = (

            self.routing_service
            .identify_agents(query)

        )
        customer_id = (
            self.routing_service.extract_customer_id(
                query
            )
        )

        self.query_logger.log_query(
            query=query,
            agents=agent_names,
            customer_id=customer_id
        )

        if not agent_names:

            return self._build_error_response(

                "Unable to determine the "
                "appropriate agent."

            )

        responses = {}

        for agent_name in agent_names:

            responses[agent_name] = (

                self._invoke_agent(

                    agent_name,

                    query,
                    correlation_id

                )

            )

        return {

            "success": True,

            "agents_invoked": agent_names,

            "responses": responses

        }

    # ---------------------------------------------------------
    # Agent Invocation
    # ---------------------------------------------------------

    def _invoke_agent(
        self,
        agent_name: str,
        query: str,
        correlation_id
    ) -> Any:
        """
        Invoke the configured
        specialist agent.
        """

        agent = self._agents[agent_name]

        handler = getattr(

            agent["instance"],

            agent["method"]

        )

        input_type = agent["input_type"]

        #
        # Customer Identifier
        #

        if input_type == self.CUSTOMER_ID_INPUT:

            customer_id = (

                self.routing_service
                .extract_customer_id(query)

            )

            if customer_id is None:

                return {

                    "success": False,

                    "message": (
                        "No valid customer ID "
                        "was found in the request."
                    ),

                    "customer_profile": None,

                    "assessment": None,

                    "risk_summary": None

                }

            return handler(customer_id)

        #
        # Natural Language Query
        #

        if input_type == self.QUERY_INPUT:

            return handler(query)

        #
        # Unsupported Input Type
        #

        return {

            "success": False,

            "message": (
                f"Unsupported input type: "
                f"{input_type}"
            )

        }

    # ---------------------------------------------------------
    # Response Helpers
    # ---------------------------------------------------------

    def _build_error_response(
        self,
        message: str
    ) -> Dict[str, Any]:
        """
        Build standardized
        error response.
        """

        return {

            "success": False,

            "message": message,

            "agents_invoked": [],

            "responses": {}

        }

    # ---------------------------------------------------------
    # Public Entry Point
    # ---------------------------------------------------------

    def process_query(
        self,
        query: str
    ) -> Dict[str, Any]:
        """
        Process a user request.
        """
        correlation_id = (
            self.execution_logger
            .create_correlation_id()
        )

        if not query.strip():

            return self._build_error_response(

                "Please provide a valid query."

            )

        start = time.perf_counter()

        success = True
        error = None

        try: 
            
            response = self.route_query(query,correlation_id=correlation_id)

        except Exception as ex:

            success = False
        
            error = str(ex)
        
            raise
        finally:

            elapsed = (
        
                time.perf_counter()
        
                - start
        
            ) * 1000

            self.execution_logger.log_execution(

                correlation_id=correlation_id,
        
                agent_name=agent_name,
        
                input_summary=query,
        
                response=response if success else {},
        
                execution_time_ms=elapsed,
        
                success=success,
        
                error_message=error
        
            )
            
        return self.response_formatter.format_response(
            response
        )


# ---------------------------------------------------------
# Test Harness
# ---------------------------------------------------------

if __name__ == "__main__":

    coordinator = CoordinatorAgent()

    query = (
        "Assess customer "
        "CUST000001 against the "
        "premium credit card policy."
    )

    response = coordinator.process_query(
        query
    )

    from pprint import pprint

    print("\nResponse")
    print("=" * 80)

    pprint(response)
