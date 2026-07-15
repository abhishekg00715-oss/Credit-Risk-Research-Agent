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

        "assessment",

        "risk_summary"
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


# ---------------------------------------------------------
# Risk Summary Contract
# ---------------------------------------------------------

def test_risk_summary_exists(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    summary = response["risk_summary"]

    assert summary is not None

    assert "overall_risk" in summary

    assert "executive_summary" in summary

    assert "strengths" in summary

    assert "risk_factors" in summary

    assert "key_observations" in summary

    assert "supporting_evidence" in summary


def test_overall_risk(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    overall_risk = response["risk_summary"]["overall_risk"]

    assert overall_risk in (

        "Low Risk",

        "Moderate Risk",

        "High Risk"
    )

def test_executive_summary(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    summary = response["risk_summary"]

    assert isinstance(
        summary["executive_summary"],
        str
    )

    assert len(
        summary["executive_summary"]
    ) > 0

def test_supporting_evidence(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    evidence = response["risk_summary"]["supporting_evidence"]

    assert isinstance(
        evidence,
        list
    )

    assert len(evidence) > 0

def test_rule_ids_not_exposed(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    summary = response["risk_summary"]

    text = str(summary)

    assert "BR-" not in text

def test_assessment_contains_rule_ids(
    customer_agent
):

    response = customer_agent.retrieve_customer_profile(
        "CUST000001"
    )

    assessment = response["assessment"]

    assert assessment["credit_score"]["rule_id"] == "BR-001"

    assert assessment["credit_utilization"]["rule_id"] == "BR-002"

    assert assessment["dti_ratio"]["rule_id"] == "BR-003"

    assert assessment["payment_history"]["rule_id"] == "BR-004"

    assert assessment["fraud_indicator"]["rule_id"] == "BR-005"

    assert assessment["overall_summary"]["rule_id"] == "BR-006"
