"""
test_policy_agent.py

Smoke tests for Policy Agent.
"""

from src.agents.policy_agent import PolicyAgent


def test_policy_agent_initialization():

    agent = PolicyAgent()

    assert agent is not None


def test_policy_query():

    agent = PolicyAgent()

    question = (
        "What is the minimum credit score "
        "required for premium credit cards?"
    )

    response = agent.answer_question(
        question
    )

    assert response is not None
    assert len(response) > 0

    print("\nAgent Response:")
    print(response)


if __name__ == "__main__":

    test_policy_agent_initialization()

    test_policy_query()

    print(
        "\n✓ Policy Agent Tests Passed"
    )