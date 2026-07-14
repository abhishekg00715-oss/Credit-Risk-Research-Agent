"""
test_customer_assessment_service.py

Unit tests for CustomerAssessmentService.

These tests validate the rule-based assessment logic
implemented by the Customer Assessment Service.

Author
------
Credit Risk Research Agent
"""

import pytest

from src.services.customer_assessment_service import (
    CustomerAssessmentService
)


@pytest.fixture
def assessment_service():
    """Create Customer Assessment Service."""

    return CustomerAssessmentService()


@pytest.fixture
def sample_customer_profile():
    """
    Sample customer profile used across tests.
    """

    return {

        "customer": {

            "customer_id": "CUST000001"
        },

        "credit_bureau": {

            "credit_score": 740,

            "credit_utilization": 33.0,

            "dti_ratio": 15.45,

            "late_payments": 0,

            "fraud_flag": "No"
        }
    }


# ---------------------------------------------------------
# BR-001
# ---------------------------------------------------------

def test_credit_score_assessment(
    assessment_service,
    sample_customer_profile
):
    """
    Verify credit score assessment.
    """

    result = assessment_service._assess_credit_score(
        sample_customer_profile
    )

    assert result["metric"] == "Credit Score"

    assert result["rating"] == "Good"

    assert result["rule_id"] == "BR-001"


# ---------------------------------------------------------
# BR-002
# ---------------------------------------------------------

def test_credit_utilization_assessment(
    assessment_service,
    sample_customer_profile
):

    result = assessment_service._assess_credit_utilization(
        sample_customer_profile
    )

    assert result["rating"] == "Moderate"

    assert result["rule_id"] == "BR-002"


# ---------------------------------------------------------
# BR-003
# ---------------------------------------------------------

def test_dti_assessment(
    assessment_service,
    sample_customer_profile
):

    result = assessment_service._assess_dti_ratio(
        sample_customer_profile
    )

    assert result["rating"] == "Low"

    assert result["rule_id"] == "BR-003"


# ---------------------------------------------------------
# BR-004
# ---------------------------------------------------------

def test_payment_history_assessment(
    assessment_service,
    sample_customer_profile
):

    result = assessment_service._assess_payment_history(
        sample_customer_profile
    )

    assert result["rating"] == "Excellent"

    assert result["rule_id"] == "BR-004"


# ---------------------------------------------------------
# BR-005
# ---------------------------------------------------------

def test_fraud_indicator_assessment(
    assessment_service,
    sample_customer_profile
):

    result = assessment_service._assess_fraud_indicator(
        sample_customer_profile
    )

    assert result["rating"] == "Clear"

    assert result["rule_id"] == "BR-005"


# ---------------------------------------------------------
# BR-006
# ---------------------------------------------------------

def test_customer_assessment(
    assessment_service,
    sample_customer_profile
):
    """
    Verify overall assessment.
    """

    result = assessment_service.assess_customer(
        sample_customer_profile
    )

    assert "overall_summary" in result

    assert result["overall_summary"]["rule_id"] == "BR-006"


# ---------------------------------------------------------
# Missing Bureau
# ---------------------------------------------------------

def test_missing_credit_bureau(
    assessment_service
):

    profile = {

        "customer": {}
    }

    result = assessment_service._assess_credit_score(
        profile
    )

    assert result["rating"] == "Unavailable"


# ---------------------------------------------------------
# Assessment Contract
# ---------------------------------------------------------

def test_assessment_contract(
    assessment_service,
    sample_customer_profile
):

    result = assessment_service._assess_credit_score(
        sample_customer_profile
    )

    expected_keys = {

        "metric",

        "value",

        "rating",

        "rule_id",

        "reason"
    }

    assert expected_keys == set(result.keys())
