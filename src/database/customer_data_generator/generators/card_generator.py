"""
card_generator.py

Purpose:
Generate synthetic credit card account
data for customers.

Author:
Credit Risk Research Agent
"""

import random

import pandas as pd

from datetime import (
    datetime,
    timedelta
)

from src.database.customer_data_generator.config import (
    CARD_PRODUCTS,
    MAX_CREDIT_CARDS
)


class CardGenerator:
    """
    Generates synthetic credit card
    account information.
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

        self.card_counter = 1

    # --------------------------------------------------
    # Card ID
    # --------------------------------------------------

    def generate_card_id(
        self
    ) -> str:

        card_id = (
            f"CARD{self.card_counter:06d}"
        )

        self.card_counter += 1

        return card_id

    # --------------------------------------------------
    # Card Product
    # --------------------------------------------------

    def determine_card_product(
        self,
        credit_score: int
    ):

        for product, rules in (
            sorted(
                CARD_PRODUCTS.items(),
                key=lambda x: x[1]["min_score"],
                reverse=True
            )
        ):

            if credit_score >= rules[
                "min_score"
            ]:

                return product

        return "Classic"

    # --------------------------------------------------
    # Number of Cards
    # --------------------------------------------------

    @staticmethod
    def number_of_cards():

        probability = random.random()

        if probability < 0.70:

            return 1

        elif probability < 0.95:

            return 2

        return MAX_CREDIT_CARDS

    # --------------------------------------------------
    # Card Status
    # --------------------------------------------------

    @staticmethod
    def card_status():

        return random.choices(

            [

                "Active",

                "Blocked",

                "Closed"

            ],

            weights=[95,3,2]

        )[0]

    # --------------------------------------------------
    # Generate DataFrame
    # --------------------------------------------------

    def generate_dataframe(
        self
    ) -> pd.DataFrame:

        bureau_lookup = (

            self.bureau_dataframe
            .set_index("customer_id")
            .to_dict("index")

        )

        card_records = []

        for _, customer in (

            self.customer_dataframe.iterrows()

        ):

            customer_id = (
                customer["customer_id"]
            )

            bureau = (
                bureau_lookup[
                    customer_id
                ]
            )

            credit_score = (
                bureau["credit_score"]
            )

            utilization = (
                bureau[
                    "credit_utilization"
                ]
            )

            annual_income = (
                customer[
                    "annual_income"
                ]
            )

            number_cards = (
                self.number_of_cards()
            )

            for _ in range(
                number_cards
            ):

                product = (
                    self.determine_card_product(
                        credit_score
                    )
                )

                rules = (
                    CARD_PRODUCTS[
                        product
                    ]
                )

                credit_limit = round(

                    annual_income *

                    rules[
                        "income_multiplier"
                    ],

                    2

                )

                outstanding = round(

                    credit_limit *

                    utilization /

                    100,

                    2

                )

                available = round(

                    credit_limit -

                    outstanding,

                    2

                )

                issue_date = (

                    datetime.today()

                    -

                    timedelta(

                        days=random.randint(
                            100,
                            2500
                        )

                    )

                )

                expiry = (

                    issue_date

                    +

                    timedelta(
                        days=365*5
                    )

                )

                card_records.append(

                    {

                        "card_id":

                            self.generate_card_id(),

                        "customer_id":

                            customer_id,

                        "card_type":

                            product,

                        "issue_date":

                            issue_date.date(),

                        "expiry_date":

                            expiry.date(),

                        "credit_limit":

                            credit_limit,

                        "available_limit":

                            available,

                        "outstanding_balance":

                            outstanding,

                        "utilization_percentage":

                            utilization,

                        "annual_fee":

                            rules[
                                "annual_fee"
                            ],

                        "card_status":

                            self.card_status()

                    }

                )

        return pd.DataFrame(
            card_records
        )


if __name__ == "__main__":

    print(
        "Run through data_pipeline_execution.py"
    )
