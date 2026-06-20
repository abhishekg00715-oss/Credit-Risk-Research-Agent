"""
test_coordinator_agent.py
"""

from src.agents.coordinator_agent import (
    CoordinatorAgent
)


def test_coordinator_agent():

    coordinator = CoordinatorAgent()

    response = coordinator.process_query(
        "What is the minimum credit score "
        "required for premium credit cards?"
    )

    assert response is not None

    print("\nResponse:")
    print(response)


if __name__ == "__main__":

    test_coordinator_agent()

    print(
        "\n✓ Coordinator Agent Test Passed"
    )