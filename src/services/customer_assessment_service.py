"""
customer_assessment_service.py

Purpose
-------
Provides rule-based assessment of customer credit information.

The service transforms raw customer data retrieved from the
Customer Repository into structured, explainable assessment
results by applying documented business rules.

Responsibilities
----------------
- Evaluate customer credit profile
- Apply business assessment rules
- Produce explainable assessment results
- Generate an overall customer risk summary

Out of Scope
------------
- Database access
- Customer retrieval
- Portfolio analysis
- Recommendation generation
- UI rendering

Business Rules
--------------
Refer:
docs/business_rules_catalogue.md

Author
------
Credit Risk Research Agent
"""

from typing import Any, Dict


class CustomerAssessmentService:
    """
    Service responsible for performing rule-based customer
    credit assessments.

    The service applies documented business rules to customer
    information supplied by the Customer Repository.

    The service is intentionally stateless and performs no
    database access.
    """

    # ---------------------------------------------------------
    # Public Interface
    # ---------------------------------------------------------

    def assess_customer(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Perform a complete assessment of a customer's credit
        profile.

        Parameters
        ----------
        customer_profile : dict
            Customer profile returned by the Customer Repository.

        Returns
        -------
        dict
            Structured customer assessment.
        """

        assessment = {

            "credit_score":
                self._assess_credit_score(customer_profile),

            "credit_utilization":
                self._assess_credit_utilization(customer_profile),

            "dti_ratio":
                self._assess_dti_ratio(customer_profile),

            "payment_history":
                self._assess_payment_history(customer_profile),

            "fraud_indicator":
                self._assess_fraud_indicator(customer_profile)
        }

        assessment["overall_summary"] = (
            self._generate_risk_summary(assessment)
        )

        return assessment

    # ---------------------------------------------------------
    # Individual Assessment Methods
    # ---------------------------------------------------------

    def _assess_credit_score(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess customer credit score.
    
        Business Rule
        -------------
        BR-001
    
        Credit Score Classification
    
        Excellent : >= 750
        Good      : 700 - 749
        Fair      : 650 - 699
        Poor      : < 650
    
        Returns
        -------
        dict
        """
    
        bureau = customer_profile.get("credit_bureau")
    
        if not bureau:
    
            return self._build_assessment(
    
                metric="Credit Score",
    
                value=None,
    
                rating="Unavailable",
    
                rule_id="BR-001",
    
                reason="Credit bureau information is unavailable."
            )
    
        credit_score = bureau.get("credit_score")
    
        if credit_score >= 750:
    
            rating = "Excellent"
    
            reason = (
                "Credit score indicates excellent creditworthiness."
            )
    
        elif credit_score >= 700:
    
            rating = "Good"
    
            reason = (
                "Credit score indicates good creditworthiness."
            )
    
        elif credit_score >= 650:
    
            rating = "Fair"
    
            reason = (
                "Credit score indicates moderate creditworthiness."
            )
    
        else:
    
            rating = "Poor"
    
            reason = (
                "Credit score indicates elevated credit risk."
            )
    
        return self._build_assessment(
    
            metric="Credit Score",
    
            value=credit_score,
    
            rating=rating,
    
            rule_id="BR-001",
    
            reason=reason
        )

    def _assess_credit_utilization(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess customer credit utilization.
    
        Business Rule
        -------------
        BR-002
    
        Utilization Classification
    
        Low       : < 30%
        Moderate  : 30% - 50%
        High      : > 50%
    
        Returns
        -------
        dict
        """
    
        bureau = customer_profile.get("credit_bureau")
    
        if not bureau:
    
            return self._build_assessment(
    
                metric="Credit Utilization",
    
                value=None,
    
                rating="Unavailable",
    
                rule_id="BR-002",
    
                reason="Credit bureau information is unavailable."
            )
    
        utilization = bureau.get("credit_utilization")
    
        if utilization < 30:
    
            rating = "Low"
    
            reason = (
                "Credit utilization is well below the recommended threshold."
            )
    
        elif utilization <= 50:
    
            rating = "Moderate"
    
            reason = (
                "Credit utilization is within an acceptable range."
            )
    
        else:
    
            rating = "High"
    
            reason = (
                "High credit utilization may indicate increased credit risk."
            )
    
        return self._build_assessment(
    
            metric="Credit Utilization",
    
            value=utilization,
    
            rating=rating,
    
            rule_id="BR-002",
    
            reason=reason
        )

    def _assess_dti_ratio(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess customer debt-to-income ratio.
    
        Business Rule
        -------------
        BR-003
    
        DTI Classification
    
        Low       : < 20%
        Moderate  : 20% - 35%
        High      : > 35%
    
        Returns
        -------
        dict
        """
    
        bureau = self._get_credit_bureau(customer_profile)
    
        if not bureau:
    
            return self._build_assessment(
    
                metric="Debt-to-Income Ratio",
    
                value=None,
    
                rating="Unavailable",
    
                rule_id="BR-003",
    
                reason="Credit bureau information is unavailable."
            )
    
        dti_ratio = bureau.get("dti_ratio")
    
        if dti_ratio < 20:
    
            rating = "Low"
    
            reason = (
                "Debt obligations are comfortably supported by income."
            )
    
        elif dti_ratio <= 35:
    
            rating = "Moderate"
    
            reason = (
                "Debt-to-income ratio is within an acceptable range."
            )
    
        else:
    
            rating = "High"
    
            reason = (
                "High debt-to-income ratio may affect repayment capacity."
            )
    
        return self._build_assessment(
    
            metric="Debt-to-Income Ratio",
    
            value=dti_ratio,
    
            rating=rating,
    
            rule_id="BR-003",
    
            reason=reason
        )

    def _assess_payment_history(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess customer payment history.
    
        Business Rule
        -------------
        BR-004
    
        Returns
        -------
        dict
        """
    
        bureau = self._get_credit_bureau(customer_profile)
    
        if not bureau:
    
            return self._build_assessment(
    
                metric="Payment History",
    
                value=None,
    
                rating="Unavailable",
    
                rule_id="BR-004",
    
                reason="Credit bureau information is unavailable."
            )
    
        late_payments = bureau.get("late_payments", 0)
    
        if late_payments == 0:
    
            rating = "Excellent"
    
            reason = (
                "No late payments recorded."
            )
    
        elif late_payments <= 2:
    
            rating = "Moderate"
    
            reason = (
                "Limited late payment history observed."
            )
    
        else:
    
            rating = "Poor"
    
            reason = (
                "Frequent late payments indicate repayment risk."
            )
    
        return self._build_assessment(
    
            metric="Payment History",
    
            value=late_payments,
    
            rating=rating,
    
            rule_id="BR-004",
    
            reason=reason
        )

    def _assess_fraud_indicator(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess customer fraud indicator.
    
        Business Rule
        -------------
        BR-005
    
        Returns
        -------
        dict
        """
    
        bureau = self._get_credit_bureau(customer_profile)
    
        if not bureau:
    
            return self._build_assessment(
    
                metric="Fraud Indicator",
    
                value=None,
    
                rating="Unavailable",
    
                rule_id="BR-005",
    
                reason="Credit bureau information is unavailable."
            )
    
        fraud_flag = bureau.get("fraud_flag")
    
        if fraud_flag == "No":
    
            rating = "Clear"
    
            reason = (
                "No fraud indicators identified."
            )
    
        else:
    
            rating = "High Risk"
    
            reason = (
                "Fraud indicator requires immediate investigation."
            )
    
        return self._build_assessment(
    
            metric="Fraud Indicator",
    
            value=fraud_flag,
    
            rating=rating,
    
            rule_id="BR-005",
    
            reason=reason
        )


    # ---------------------------------------------------------
# Data Extraction Helpers
# ---------------------------------------------------------

    def _get_credit_bureau(
        self,
        customer_profile: Dict[str, Any]
    ) -> Dict[str, Any] | None:
        """
        Retrieve credit bureau information from the customer profile.

        Parameters
        ----------
        customer_profile : dict

        Returns
        -------
        dict | None
            Credit bureau information if available.
        """

        return customer_profile.get("credit_bureau")
    # ---------------------------------------------------------
    # Assessment Helpers
    # ---------------------------------------------------------

    def _generate_risk_summary(
        self,
        assessment: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate an overall customer risk summary.
    
        Business Rule
        -------------
        BR-006
    
        Returns
        -------
        dict
        """
    
        ratings = [
    
            assessment["credit_score"]["rating"],
    
            assessment["credit_utilization"]["rating"],
    
            assessment["dti_ratio"]["rating"],
    
            assessment["payment_history"]["rating"],
    
            assessment["fraud_indicator"]["rating"]
        ]
    
        reasons = []
    
        high_risk_count = 0
        moderate_count = 0
    
        for item in assessment.values():
    
            if not isinstance(item, dict):
                continue
    
            reasons.append(item.get("reason"))
    
            rating = item.get("rating")
    
            if rating in ("Poor", "High", "High Risk"):
    
                high_risk_count += 1
    
            elif rating == "Moderate":
    
                moderate_count += 1
    
        # --------------------------------------------------
        # Overall Assessment
        # --------------------------------------------------
    
        if assessment["fraud_indicator"]["rating"] == "High Risk":
    
            overall_rating = "High Risk"
    
        elif assessment["credit_score"]["rating"] == "Poor":
    
            overall_rating = "High Risk"
    
        elif high_risk_count >= 2:
    
            overall_rating = "High Risk"
    
        elif high_risk_count == 1:
    
            overall_rating = "Moderate Risk"
    
        elif moderate_count >= 2:
    
            overall_rating = "Moderate Risk"
    
        else:
    
            overall_rating = "Low Risk"
    
        return {
    
            "metric": "Overall Customer Assessment",
    
            "rating": overall_rating,
    
            "rule_id": "BR-006",
    
            "reason": reasons
        }

    def _build_assessment(
        self,
        metric: str,
        value: Any,
        rating: str,
        rule_id: str,
        reason: str
    ) -> Dict[str, Any]:
        """
        Construct a standardized assessment object.

        Parameters
        ----------
        metric : str
            Assessment metric.

        value : Any
            Raw metric value.

        rating : str
            Assigned rating.

        rule_id : str
            Business Rule identifier.

        reason : str
            Explainable rationale.

        Returns
        -------
        dict
        """

        return {

            "metric": metric,

            "value": value,

            "rating": rating,

            "rule_id": rule_id,

            "reason": reason
        }

# ------------------------------------------------------------------
# Test Harness
# ------------------------------------------------------------------

if __name__ == "__main__":

    from repository.customer_repository import CustomerRepository

    repository = CustomerRepository()

    customer_profile = repository.get_customer_profile(
        "CUST000001"
    )

    service = CustomerAssessmentService()

    assessment = service.assess_customer(customer_profile)

    print("\nCustomer Assessment")
    print("-" * 60)

    for key, value in assessment.items():

        print(f"\n{key}")

        print(value)
