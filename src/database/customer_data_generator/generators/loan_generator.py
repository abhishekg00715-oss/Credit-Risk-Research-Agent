"""
loan_generator.py

Purpose:
Generate synthetic loan account data
for each eligible customer.

Author:
Credit Risk Research Agent
"""

import random
import math

import pandas as pd

from datetime import (
    datetime,
    timedelta
)

from src.database.customer_data_generator.config import (
    MAX_LOANS,
    LOAN_PRODUCTS,
    LOAN_STATUS
)

from src.database.customer_data_generator.generators.customer_generator import (
    CustomerGenerator,
)
from src.database.customer_data_generator.generators.bureau_generator import (
    BureauGenerator,
)

class LoanGenerator:
    """
    Generate synthetic
    loan account information.
    """

    def __init__(
        self,
        customer_dataframe: pd.DataFrame,
        bureau_dataframe: pd.DataFrame,
        seed: int = 42
    ):

        self.customer_dataframe = (
            customer_dataframe
        )

        self.bureau_dataframe = (
            bureau_dataframe
        )

        random.seed(seed)

    # ----------------------------------------
    # Loan ID
    # ----------------------------------------

    @staticmethod
    def generate_loan_id(
        loan_number: int
    ) -> str:

        return (
            f"LOAN{loan_number:08d}"
        )

    # ----------------------------------------
    # Number of Loans
    # ----------------------------------------

    @staticmethod
    def number_of_loans(
        credit_score: int
    ) -> int:
        """
        Higher credit score customers
        have a greater probability of
        holding multiple loans.
        """

        if credit_score >= 780:

            probabilities = list(
                range(
                    MAX_LOANS + 1
                )
            )

            weights = [
                20,
                45,
                35
            ]

        elif credit_score >= 700:

            probabilities = list(
                range(
                    MAX_LOANS + 1
                )
            )

            weights = [
                35,
                50,
                15
            ]

        else:

            probabilities = list(
                range(
                    MAX_LOANS + 1
                )
            )

            weights = [
                60,
                40
            ]

        loans = random.choices(
            probabilities,
            weights=weights,
            k=1
        )[0]

        return min(
            loans,
            MAX_LOANS
        )

    # ----------------------------------------
    # Loan Product
    # ----------------------------------------

    @staticmethod
    def determine_loan_product(
        credit_score: int
    ) -> str:
        """
        Select a loan product
        based on bureau score.
        """

        eligible_products = [

            product

            for product, details

            in LOAN_PRODUCTS.items()

            if credit_score >=
            details["min_score"]

        ]

        if not eligible_products:

            return "Personal Loan"

        return random.choice(
            eligible_products
        )

    # ----------------------------------------
    # Payment Behaviour
    # ----------------------------------------

    @staticmethod
    def determine_payment_behaviour(
        credit_score: int
    ):
        """
        Determine repayment
        behaviour based on
        bureau score.
        """

        if credit_score >= 780:

            return (
                "On Time",
                0
            )

        elif credit_score >= 720:

            return (
                random.choice(
                    [
                        "On Time",
                        "On Time",
                        "Delayed"
                    ]
                ),
                random.choice(
                    [
                        0,
                        0,
                        15
                    ]
                )
            )

        elif credit_score >= 650:

            return (
                random.choice(
                    [
                        "On Time",
                        "Delayed"
                    ]
                ),
                random.choice(
                    [
                        0,
                        15,
                        30
                    ]
                )
            )

        return (
            "Delayed",
            random.choice(
                [
                    30,
                    60,
                    90
                ]
            )
        )

    # ----------------------------------------
    # EMI Calculation
    # ----------------------------------------

    @staticmethod
    def calculate_emi(
        principal: float,
        annual_interest: float,
        tenure_months: int
    ) -> float:
        """
        Standard EMI calculation.
        """

        monthly_rate = (
            annual_interest / 12 / 100
        )

        if monthly_rate == 0:

            return round(
                principal /
                tenure_months,
                2
            )

        emi = (

            principal *

            monthly_rate *

            math.pow(
                1 + monthly_rate,
                tenure_months
            )

        ) / (

            math.pow(
                1 + monthly_rate,
                tenure_months
            ) - 1

        )

        return round(
            emi,
            2
        )

    # ----------------------------------------
    # Generate DataFrame
    # ----------------------------------------

    def generate_dataframe(
        self
    ) -> pd.DataFrame:

        loan_records = []

        loan_number = 1

        bureau_lookup = (
            self.bureau_dataframe
            .set_index("customer_id")
            .to_dict("index")
        )

        for _, customer in (
            self.customer_dataframe.iterrows()
        ):

            customer_id = (
                customer["customer_id"]
            )

            bureau = (
                bureau_lookup.get(
                    customer_id
                )
            )

            if bureau is None:
                continue

            credit_score = (
                bureau["credit_score"]
            )

            annual_income = (
                customer["annual_income"]
            )

            number_of_loans = (
                self.number_of_loans(
                    credit_score
                )
            )

            if number_of_loans == 0:
                continue

            for _ in range(
                number_of_loans
            ):

                loan_product = (
                    self.determine_loan_product(
                        credit_score
                    )
                )

                product = (
                    LOAN_PRODUCTS[
                        loan_product
                    ]
                )

                max_amount = (

                    annual_income *

                    product[
                        "max_income_multiplier"
                    ]

                )

                sanctioned_amount = round(

                    random.uniform(
                        max_amount * 0.40,
                        max_amount
                    ),

                    2

                )

                interest_rate = round(

                    random.uniform(

                        product[
                            "interest_range"
                        ][0],

                        product[
                            "interest_range"
                        ][1]

                    ),

                    2

                )

                if loan_product == "Home Loan":

                    tenure = random.choice(
                        [
                            180,
                            240,
                            300
                        ]
                    )

                elif loan_product == "Auto Loan":

                    tenure = random.choice(
                        [
                            36,
                            48,
                            60,
                            72
                        ]
                    )

                elif loan_product == "Education Loan":

                    tenure = random.choice(
                        [
                            60,
                            84,
                            120
                        ]
                    )

                else:

                    tenure = random.choice(
                        [
                            24,
                            36,
                            48,
                            60
                        ]
                    )

                emi = (
                    self.calculate_emi(
                        sanctioned_amount,
                        interest_rate,
                        tenure
                    )
                )

                remaining_tenure = (
                    random.randint(
                        1,
                        tenure
                    )
                )

                outstanding_balance = round(

                    sanctioned_amount *

                    remaining_tenure /

                    tenure,

                    2

                )

                payment_status, dpd = (

                    self.determine_payment_behaviour(
                        credit_score
                    )

                )

                disbursement_date = (

                    datetime.today()

                    -

                    timedelta(
                        days=random.randint(
                            180,
                            tenure * 30
                        )
                    )

                ).date()

                maturity_date = (

                    disbursement_date

                    +

                    timedelta(
                        days=tenure * 30
                    )

                )

                loan_records.append(

                    {

                        "loan_id":
                            self.generate_loan_id(
                                loan_number
                            ),

                        "customer_id":
                            customer_id,

                        "loan_type":
                            loan_product,

                        "loan_status":
                            random.choice(
                                LOAN_STATUS
                            ),

                        "secured":
                            product[
                                "secured"
                            ],

                        "sanctioned_amount":
                            sanctioned_amount,

                        "outstanding_balance":
                            outstanding_balance,

                        "interest_rate":
                            interest_rate,

                        "tenure_months":
                            tenure,

                        "remaining_tenure":
                            remaining_tenure,

                        "monthly_emi":
                            emi,

                        "repayment_status":
                            payment_status,

                        "days_past_due":
                            dpd,

                        "disbursement_date":
                            disbursement_date,

                        "maturity_date":
                            maturity_date

                    }

                )

                loan_number += 1

        return pd.DataFrame(
            loan_records
        )

# ----------------------------------------
# Local Testing
# ----------------------------------------

if __name__ == "__main__":

    customer_df = (
        CustomerGenerator(
            number_of_customers=10
        ).generate_dataframe()
    )

    bureau_df = (
        BureauGenerator(
            customer_dataframe=customer_df
        ).generate_dataframe()
    )

    loan_df = (
        LoanGenerator(
            customer_dataframe=customer_df,
            bureau_dataframe=bureau_df
        ).generate_dataframe()
    )

    print(loan_df.head())

    print()

    print(loan_df.info())
