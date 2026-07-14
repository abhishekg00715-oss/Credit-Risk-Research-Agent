"""
test_customer_agent.py

Integration tests for Customer Agent.

Author
------
Credit Risk Research Agent
"""

import pytest

from src.agents.customer_agent import CustomerAgent


@pytest.fixture
def customer_agent():
    """
    Create Customer Agent.
    """

    return CustomerAgent()


# ---------------------------------------------------------
# Valid Customer
# ---------------------------------------------------------

def test_valid_customer_retrieval(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    assert response["success"] is True

    assert response["customer_profile"] is not None

    assert response["assessment"] is not None


# ---------------------------------------------------------
# Empty Customer ID
# ---------------------------------------------------------

def test_empty_customer_id(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        ""
    )

    assert response["success"] is False

    assert "cannot be empty" in response["message"]


# ---------------------------------------------------------
# Invalid Customer
# ---------------------------------------------------------

def test_unknown_customer(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "UNKNOWN"
    )

    assert response["success"] is False

    assert response["customer_profile"] is None


# ---------------------------------------------------------
# Response Contract
# ---------------------------------------------------------

def test_response_contract(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    expected = {

        "success",

        "message",

        "customer_profile",

        "assessment"
    }

    assert expected == set(response.keys())


# ---------------------------------------------------------
# Customer Profile Contract
# ---------------------------------------------------------

def test_customer_profile_contract(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    profile = response["customer_profile"]

    assert "customer" in profile

    assert "credit_bureau" in profile

    assert "credit_cards" in profile

    assert "loans" in profile

    assert "transactions" in profile

    assert "digital_behavior" in profile


# ---------------------------------------------------------
# Assessment Contract
# ---------------------------------------------------------

def test_assessment_exists(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    assessment = response["assessment"]

    assert "credit_score" in assessment

    assert "credit_utilization" in assessment

    assert "dti_ratio" in assessment

    assert "payment_history" in assessment

    assert "fraud_indicator" in assessment

    assert "overall_summary" in assessment
