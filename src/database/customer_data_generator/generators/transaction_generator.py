"""
transaction_generator.py

Purpose:
Generate synthetic banking transactions
for each customer.

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
    MIN_TRANSACTIONS,
    MAX_TRANSACTIONS,
    DEBIT_TRANSACTION_CATEGORIES,
    CREDIT_TRANSACTION_CATEGORIES,
    TRANSACTION_CHANNELS
)


class TransactionGenerator:
    """
    Generate synthetic customer
    transaction history.
    """

    def __init__(
        self,
        customer_dataframe: pd.DataFrame,
        bureau_dataframe: pd.DataFrame | None = None,
        card_dataframe: pd.DataFrame | None = None,
        loan_dataframe: pd.DataFrame | None = None,
        seed: int = 42
    ):

        self.customer_dataframe = (
            customer_dataframe
        )

        self.bureau_dataframe = (
            bureau_dataframe
        )

        self.card_dataframe = (
            card_dataframe
        )

        self.loan_dataframe = (
            loan_dataframe
        )

        random.seed(seed)

    # ----------------------------------------
    # Transaction ID
    # ----------------------------------------

    @staticmethod
    def generate_transaction_id(
        transaction_number: int
    ) -> str:

        return (
            f"TXN{transaction_number:010d}"
        )

    # ----------------------------------------
    # Number of Transactions
    # ----------------------------------------

    @staticmethod
    def number_of_transactions(
        annual_income: float
    ) -> int:
        """
        Higher income customers generally
        perform more banking transactions.
        """

        if annual_income >= 2500000:

            return random.randint(
                90,
                MAX_TRANSACTIONS
            )

        elif annual_income >= 1200000:

            return random.randint(
                70,
                100
            )

        return random.randint(
            MIN_TRANSACTIONS,
            70
        )

    # ----------------------------------------
    # Merchant Category
    # ----------------------------------------
    @staticmethod
    def transaction_category(
        transaction_type: str,has_loan: bool = False
    ) -> str:
        """
        Select merchant category based
        on transaction type.
        """
    
        if transaction_type == "Credit":
    
            categories = dict(
                CREDIT_TRANSACTION_CATEGORIES
            )
            if not has_loan:

                categories.pop(
                    "Loan Disbursement",
                    None
                )
            
        else:
    
            categories = dict(
                DEBIT_TRANSACTION_CATEGORIES
            )
            if has_loan:

                categories["Loan EMI"] = 8
        
        return random.choices(
    
            list(categories.keys()),
    
            weights=list(
                categories.values()
            ),
    
            k=1
    
        )[0]
        

    # ----------------------------------------
    # Transaction Channel
    # ----------------------------------------

    @staticmethod
    def transaction_channel():

        return random.choices(

            TRANSACTION_CHANNELS,

            weights=[
                45,    # UPI
                15,    # POS
                5,     # ATM
                10,    # Internet Banking
                25     # Mobile Banking
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Transaction Type
    # ----------------------------------------

    @staticmethod
    def transaction_type():

        return random.choices(

            [
                "Debit",
                "Credit"
            ],

            weights=[
                85,
                15
            ],

            k=1

        )[0]


    # ----------------------------------------
    # Transaction Amount
    # ----------------------------------------

    @staticmethod
    def transaction_amount(
        annual_income: float,
        transaction_type: str
    ) -> float:
        """
        Transaction amount correlated
        with customer income.
        """

        if transaction_type == "Credit":

            if annual_income >= 2500000:

                amount = random.uniform(
                    25000,
                    250000
                )

            elif annual_income >= 1200000:

                amount = random.uniform(
                    10000,
                    100000
                )

            else:

                amount = random.uniform(
                    5000,
                    50000
                )

        else:

            if annual_income >= 2500000:

                amount = random.uniform(
                    1000,
                    30000
                )

            elif annual_income >= 1200000:

                amount = random.uniform(
                    500,
                    15000
                )

            else:

                amount = random.uniform(
                    100,
                    6000
                )

        return round(
            amount,
            2
        )

    # ----------------------------------------
    # Transaction Status
    # ----------------------------------------

    @staticmethod
    def transaction_status():

        return random.choices(

            [
                "Success",
                "Failed"
            ],

            weights=[
                98,
                2
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Transaction Date
    # ----------------------------------------

    @staticmethod
    def transaction_date():

        return (

            datetime.today()

            -

            timedelta(

                days=random.randint(
                    1,
                    365
                )

            )

        ).date()

    # ----------------------------------------
    # Account Type
    # ----------------------------------------

    @staticmethod
    def account_type(
        has_card: bool,
        has_loan: bool
    ) -> str:
        """
        Identify the primary account
        associated with the transaction.
        """

        account_types = [
            "Savings Account"
        ]

        if has_card:

            account_types.append(
                "Credit Card"
            )

        if has_loan:

            account_types.append(
                "Loan Account"
            )

        return random.choice(
            account_types
        )


    # ----------------------------------------
    # Generate DataFrame
    # ----------------------------------------

    def generate_dataframe(
        self
    ) -> pd.DataFrame:

        transaction_records = []

        transaction_number = 1

        card_lookup = (
            self.card_dataframe
            .groupby("customer_id")
            .size()
            .to_dict()
        )

        loan_lookup = (
            self.loan_dataframe
            .groupby("customer_id")
            .size()
            .to_dict()
        )

        for _, customer in (
            self.customer_dataframe.iterrows()
        ):

            customer_id = (
                customer["customer_id"]
            )

            annual_income = (
                customer["annual_income"]
            )

            customer_state = (
                customer["state"]
            )

            has_card = (
                customer_id in card_lookup
            )

            has_loan = (
                customer_id in loan_lookup
            )

            total_transactions = (

                self.number_of_transactions(
                    annual_income
                )

            )

            for _ in range(
                total_transactions
            ):

                txn_type = (
                    self.transaction_type()
                )

                category = (
                    self.transaction_category(transaction_type=txn_type,
                        has_loan=has_loan)
                )

                amount = (
                    self.transaction_amount(
                        annual_income,
                        txn_type
                    )
                )

                channel = (
                    self.transaction_channel()
                )

                account_type = (
                    self.account_type(
                        has_card,
                        has_loan
                    )
                )

                transaction_records.append(

                    {

                        "transaction_id":
                            self.generate_transaction_id(
                                transaction_number
                            ),

                        "customer_id":
                            customer_id,

                        "account_type":
                            account_type,

                        "transaction_date":
                            self.transaction_date(),

                        "transaction_type":
                            txn_type,

                        "merchant_category":
                            category,

                        "transaction_channel":
                            channel,

                        "transaction_amount":
                            amount,

                        "transaction_status":
                            self.transaction_status(),

                        "state":
                            customer_state

                    }

                )

                transaction_number += 1

        return pd.DataFrame(
            transaction_records
        )


# ----------------------------------------
# Local Testing
# ----------------------------------------

if __name__ == "__main__":

    print(
        "Run through data_pipeline_execution.py"
    )
