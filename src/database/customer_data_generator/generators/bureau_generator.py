"""
bureau_generator.py

Purpose:
Generate synthetic credit bureau data
for each customer.

Author:
Credit Risk Research Agent
"""

import random

import pandas as pd

from datetime import datetime

from src.database.customer_data_generator.config import (
    EXCELLENT_SCORE,
    VERY_GOOD_SCORE,
    GOOD_SCORE,
    FAIR_SCORE,
    POOR_SCORE
)


class BureauGenerator:
    """
    Generate credit bureau
    information.
    """

    def __init__(
        self,
        customer_dataframe: pd.DataFrame,
        seed: int = 42
    ):

        self.customer_dataframe = (
            customer_dataframe
        )

        random.seed(seed)

    # ----------------------------------------
    # Bureau Rating
    # ----------------------------------------

    @staticmethod
    def determine_rating(
        score: int
    ) -> str:

        if score >= 800:
            return "Excellent"

        elif score >= 750:
            return "Very Good"

        elif score >= 700:
            return "Good"

        elif score >= 650:
            return "Fair"

        return "Poor"

    # ----------------------------------------
    # Generate Credit Score
    # ----------------------------------------

    def generate_credit_score(
        self,
        income: float
    ):

        if income >= 2500000:

            return random.randint(
                *EXCELLENT_SCORE
            )

        elif income >= 1500000:

            return random.randint(
                *VERY_GOOD_SCORE
            )

        elif income >= 800000:

            return random.randint(
                *GOOD_SCORE
            )

        elif income >= 500000:

            return random.randint(
                *FAIR_SCORE
            )

        return random.randint(
            *POOR_SCORE
        )

    # ----------------------------------------
    # Utilization
    # ----------------------------------------

    @staticmethod
    def utilization_from_score(
        score: int
    ):

        if score >= 800:
            return random.randint(10,25)

        elif score >= 750:
            return random.randint(20,35)

        elif score >= 700:
            return random.randint(30,50)

        elif score >= 650:
            return random.randint(40,70)

        return random.randint(70,95)

    # ----------------------------------------
    # Generate DataFrame
    # ----------------------------------------

    def generate_dataframe(
        self
    ):

        bureau_records = []

        for _, customer in (
            self.customer_dataframe.iterrows()
        ):

            income = (
                customer["annual_income"]
            )

            score = (
                self.generate_credit_score(
                    income
                )
            )

            utilization = (
                self.utilization_from_score(
                    score
                )
            )

            outstanding = (
                round(
                    income *
                    utilization / 100,
                    2
                )
            )

            dti = round(
                random.uniform(
                    15,
                    utilization
                ),
                2
            )

            bureau_records.append(

                {

                    "customer_id":
                        customer["customer_id"],

                    "credit_score":
                        score,

                    "bureau_rating":
                        self.determine_rating(
                            score
                        ),

                    "total_accounts":
                        random.randint(2,8),

                    "active_accounts":
                        random.randint(1,6),

                    "credit_utilization":
                        utilization,

                    "total_outstanding":
                        outstanding,

                    "dti_ratio":
                        dti,

                    "hard_inquiries":
                        random.randint(0,4),

                    "late_payments":
                        random.randint(
                            0,
                            2 if score > 700 else 6
                        ),

                    "defaults":
                        random.randint(
                            0,
                            0 if score > 750 else 2
                        ),

                    "bankruptcies":
                        0 if score > 680 else random.randint(0,1),

                    "fraud_flag":
                        random.choice(
                            [
                                "No",
                                "No",
                                "No",
                                "Yes"
                            ]
                        ),

                    "last_bureau_refresh":
                        datetime.today().date()
                }

            )

        return pd.DataFrame(
            bureau_records
        )


if __name__ == "__main__":

    print(
        "Run through data_pipeline_execution.py"
    )
