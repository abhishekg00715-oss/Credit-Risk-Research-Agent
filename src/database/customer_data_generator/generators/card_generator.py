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
# Payment Behaviour
# --------------------------------------------------

    
    def determine_payment_behaviour(
        self,
        credit_score: int
    ) -> dict:
        """
        Determine customer payment behaviour
        based on credit score.
    
        Returns a dictionary containing
        payment behaviour attributes used
        throughout the Card Generator.
        """
    
        # ------------------------------------------
        # Excellent Customer
        # ------------------------------------------
    
        if credit_score >= 800:
    
            return {
    
                "payment_status": "On Time",
    
                "days_past_due": 0,
    
                "missed_payments": 0,
    
                "write_off_flag": "No"
    
            }
    
        # ------------------------------------------
        # Very Good Customer
        # ------------------------------------------
    
        elif credit_score >= 750:
    
            dpd = random.randint(
                0,
                5
            )
    
            return {
    
                "payment_status":
    
                    "On Time"
    
                    if dpd == 0
    
                    else
    
                    "Grace Period",
    
                "days_past_due":
    
                    dpd,
    
                "missed_payments":
    
                    0,
    
                "write_off_flag":
    
                    "No"
    
            }
    
        # ------------------------------------------
        # Average Customer
        # ------------------------------------------
    
        elif credit_score >= 700:
    
            dpd = random.randint(
                5,
                30
            )
    
            missed = random.randint(
                1,
                3
            )
    
            return {
    
                "payment_status": "Delayed",
    
                "days_past_due": dpd,
    
                "missed_payments": missed,
    
                "write_off_flag": "No"
    
            }
    
        # ------------------------------------------
        # High Risk Customer
        # ------------------------------------------
    
        elif credit_score >= 650:
    
            dpd = random.randint(
                30,
                90
            )
    
            missed = random.randint(
                3,
                6
            )
    
            return {
    
                "payment_status": "Missed",
    
                "days_past_due": dpd,
    
                "missed_payments": missed,
    
                "write_off_flag": "No"
    
            }
    
        # ------------------------------------------
        # Default Risk Customer
        # ------------------------------------------
    
        else:
    
            dpd = random.randint(
                91,
                180
            )
    
            missed = random.randint(
                6,
                12
            )
    
            return {
    
                "payment_status": "Default",
    
                "days_past_due": dpd,
    
                "missed_payments": missed,
    
                "write_off_flag": "Yes"
    
            }
    

    # --------------------------------------------------
    # Statement Information
    # --------------------------------------------------
    
    def calculate_statement_details(
        self,
        outstanding_balance: float
    ):
    
        statement_balance = round(
    
            outstanding_balance *
    
            random.uniform(
                0.95,
                1.05
            ),
    
            2
    
        )
    
        minimum_due = round(
    
            statement_balance * 0.05,
    
            2
    
        )
    
        payment_amount = round(
    
            statement_balance *
    
            random.uniform(
                0.40,
                1.00
            ),
    
            2
    
        )
    
        return (
    
            statement_balance,
    
            minimum_due,
    
            payment_amount
    
        )
    

    # --------------------------------------------------
    # Rewards
    # --------------------------------------------------
    
    def calculate_rewards(
        self,
        card_type: str,
        outstanding_balance: float
    ):
    
        reward_program = REWARD_PROGRAMS[
            card_type
        ]
    
        reward_points = int(
    
            outstanding_balance /
    
            100
    
        )
    
        return (
    
            reward_program,
    
            reward_points
    
        )
    
    

    
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
                    
                payment = (

                    self.determine_payment_behaviour(
                
                        credit_score
                
                    )
                
                )
                
                statement_balance, minimum_due, last_payment = (
                
                    self.calculate_statement_details(
                
                        outstanding
                
                    )
                
                )
                
                reward_program, reward_points = (
                
                    self.calculate_rewards(
                
                        product,
                
                        outstanding
                
                    )
                
                )
                
                billing_day = random.choice(
                
                    BILLING_CYCLE_DAYS
                
                )
                
                payment_due = (
                
                    datetime.today()
                
                    +
                
                    timedelta(days=15)
                
                ).date()
                
                last_payment_date = (
                
                    datetime.today()
                
                    -
                
                    timedelta(
                
                        days=random.randint(
                            1,
                            30
                        )
                
                    )
                
                ).date()
  
                
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
                        

                        "cash_limit":

                            round(
                                credit_limit * 0.30,
                                2
                            ),
                        
                        "statement_balance":
                        
                            statement_balance,
                        
                        "billing_cycle_day":
                        
                            billing_day,
                        
                        "minimum_due":
                        
                            minimum_due,
                        
                        "payment_due_date":
                        
                            payment_due,
                        
                        "last_payment_amount":
                        
                            last_payment,
                        
                        "last_payment_date":
                        
                            last_payment_date,

                        "payment_status":

                            payment["payment_status"],
                        
                        "days_past_due":
                        
                            payment["days_past_due"],
                        
                        "missed_payments_last_12m":
                        
                            payment["missed_payments"],
                        
                        "write_off_flag":
                        
                            payment["write_off_flag"],
                        
                        
                        "reward_program":
                        
                            reward_program,
                        
                        "reward_points":
                        
                            reward_points,
                        
                        "last_card_transaction_date":
                        
                            datetime.today().date()
                            -
                            timedelta(
                                days=random.randint(
                                    1,
                                    20
                                )
                        )
                        
                        
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
