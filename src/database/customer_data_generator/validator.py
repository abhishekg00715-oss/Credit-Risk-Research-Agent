"""
validator.py

Purpose:
Validate referential integrity and
basic business rules for the
Synthetic Customer Data Generator.

Author:
Credit Risk Research Agent
"""

import pandas as pd


class DataValidator:
    """
    Performs validation checks
    across all generated datasets.
    """

    def __init__(
        self,
        customer_dataframe: pd.DataFrame,
        bureau_dataframe: pd.DataFrame,
        card_dataframe: pd.DataFrame,
        loan_dataframe: pd.DataFrame,
        transaction_dataframe: pd.DataFrame,
        digital_behavior_dataframe: pd.DataFrame
    ):

        self.customer_df = customer_dataframe

        self.bureau_df = bureau_dataframe

        self.card_df = card_dataframe

        self.loan_df = loan_dataframe

        self.transaction_df = transaction_dataframe

        self.digital_df = (
            digital_behavior_dataframe
        )

        self.errors = []

    # ----------------------------------------
    # Customer Lookup
    # ----------------------------------------

    @property
    def customer_ids(self):

        return set(

            self.customer_df[
                "customer_id"
            ]

        )

    # ----------------------------------------
    # Validate Customer Reference
    # ----------------------------------------

    def validate_customer_reference(
        self,
        dataframe: pd.DataFrame,
        dataframe_name: str
    ):

        invalid_ids = (

            set(
                dataframe["customer_id"]
            )

            -

            self.customer_ids

        )

        if invalid_ids:

            self.errors.append(

                f"{dataframe_name}: "

                f"{len(invalid_ids)} "

                "invalid customer_id(s)."

            )


      
    # ----------------------------------------
    # Validate Bureau Records
    # ----------------------------------------

    def validate_bureau(
        self
    ):

        self.validate_customer_reference(
            self.bureau_df,
            "Credit Bureau"
        )

        if len(self.bureau_df) != len(
            self.customer_df
        ):

            self.errors.append(

                "Credit Bureau: "

                "One bureau record "

                "expected per customer."

            )

    # ----------------------------------------
    # Validate Card Records
    # ----------------------------------------

    def validate_cards(
        self
    ):

        self.validate_customer_reference(

            self.card_df,

            "Credit Card"

        )

        duplicate_cards = (

            self.card_df[
                "card_number"
            ].duplicated().sum()

        )

        if duplicate_cards > 0:

            self.errors.append(

                f"Credit Card: "

                f"{duplicate_cards} "

                "duplicate card_number(s)."

            )

    # ----------------------------------------
    # Validate Loan Records
    # ----------------------------------------

    def validate_loans(
        self
    ):

        self.validate_customer_reference(

            self.loan_df,

            "Loan"

        )

        duplicate_loans = (

            self.loan_df[
                "loan_account_number"
            ].duplicated().sum()

        )

        if duplicate_loans > 0:

            self.errors.append(

                f"Loan: "

                f"{duplicate_loans} "

                "duplicate loan_account_number(s)."

            )

    # ----------------------------------------
    # Validate Transactions
    # ----------------------------------------

    def validate_transactions(
        self
    ):

        self.validate_customer_reference(

            self.transaction_df,

            "Transaction"

        )

        duplicate_transactions = (

            self.transaction_df[
                "transaction_id"
            ].duplicated().sum()

        )

        if duplicate_transactions > 0:

            self.errors.append(

                f"Transaction: "

                f"{duplicate_transactions} "

                "duplicate transaction_id(s)."

            )

    # ----------------------------------------
    # Validate Digital Behaviour
    # ----------------------------------------

    def validate_digital_behavior(
        self
    ):

        self.validate_customer_reference(

            self.digital_df,

            "Digital Behaviour"

        )

        duplicate_sessions = (

            self.digital_df[
                "session_id"
            ].duplicated().sum()

        )

        if duplicate_sessions > 0:

            self.errors.append(

                f"Digital Behaviour: "

                f"{duplicate_sessions} "

                "duplicate session_id(s)."

            )

    # ----------------------------------------
    # Run All Validations
    # ----------------------------------------

    def validate(
        self
    ):

        self.validate_bureau()

        self.validate_cards()

        self.validate_loans()

        self.validate_transactions()

        self.validate_digital_behavior()

        return len(
            self.errors
        ) == 0

    # ----------------------------------------
    # Validation Summary
    # ----------------------------------------

    def validation_summary(
        self
    ):

        if not self.errors:

            print()

            print(
                "=" * 50
            )

            print(
                "VALIDATION PASSED"
            )

            print(
                "=" * 50
            )

            return

        print()

        print(
            "=" * 50
        )

        print(
            "VALIDATION FAILED"
        )

        print(
            "=" * 50
        )

        for error in self.errors:

            print(
                f"- {error}"
            )

    # ----------------------------------------
    # Local Testing
    # ----------------------------------------

if __name__ == "__main__":

    print(

        "Run through "

        "data_pipeline_execution.py"

    )
