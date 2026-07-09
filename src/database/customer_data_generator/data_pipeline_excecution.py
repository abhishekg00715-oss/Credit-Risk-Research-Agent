"""
data_pipeline_execution.py

Purpose:
Execute the complete synthetic
customer data generation pipeline.

Author:
Credit Risk Research Agent
"""

from src.database.customer_data_generator.config import (

    NUMBER_OF_CUSTOMERS,

    RANDOM_SEED

)

from src.database.customer_data_generator.generators.customer_generator import (
    CustomerGenerator
)

from src.database.customer_data_generator.generators.bureau_generator import (
    BureauGenerator
)

from src.database.customer_data_generator.generators.card_generator import (
    CardGenerator
)

from src.database.customer_data_generator.generators.loan_generator import (
    LoanGenerator
)

from src.database.customer_data_generator.generators.transaction_generator import (
    TransactionGenerator
)

from src.database.customer_data_generator.generators.digital_behavior_generator import (
    DigitalBehaviorGenerator
)

from src.database.customer_data_generator.validator import (
    DataValidator
)

from src.database.customer_data_generator.exporter import (
    DataExporter
)


class CustomerDataPipeline:
    """
    Executes the complete
    customer data generation pipeline.
    """

    def __init__(

        self,

        number_of_customers: int = NUMBER_OF_CUSTOMERS,

        seed: int = RANDOM_SEED

    ):

        self.number_of_customers = (

            number_of_customers

        )

      
        self.seed = seed


    # ----------------------------------------
    # Execute Pipeline
    # ----------------------------------------

    def run(
        self
    ):

        print()

        print("=" * 60)

        print(
            "CUSTOMER DATA GENERATION PIPELINE"
        )

        print("=" * 60)

        # ----------------------------------------
        # Customer Master
        # ----------------------------------------

        customer_df = (

            CustomerGenerator(

                number_of_customers=self.number_of_customers,

                seed=self.seed

            ).generate_dataframe()

        )

        # ----------------------------------------
        # Credit Bureau
        # ----------------------------------------

        bureau_df = (

            BureauGenerator(

                customer_dataframe=customer_df,

                seed=self.seed

            ).generate_dataframe()

        )

        # ----------------------------------------
        # Credit Cards
        # ----------------------------------------

        card_df = (

            CardGenerator(

                customer_dataframe=customer_df,

                bureau_dataframe=bureau_df,

                seed=self.seed

            ).generate_dataframe()

        )

        # ----------------------------------------
        # Loan Accounts
        # ----------------------------------------

        loan_df = (

            LoanGenerator(

                customer_dataframe=customer_df,

                bureau_dataframe=bureau_df,

                seed=self.seed

            ).generate_dataframe()

        )

        # ----------------------------------------
        # Transactions
        # ----------------------------------------

        transaction_df = (

            TransactionGenerator(

                customer_dataframe=customer_df,

                card_dataframe=card_df,

                loan_dataframe=loan_df,

                seed=self.seed

            ).generate_dataframe()

        )

        # ----------------------------------------
        # Digital Behaviour
        # ----------------------------------------

        digital_df = (

            DigitalBehaviorGenerator(

                customer_dataframe=customer_df,

                transaction_dataframe=transaction_df,

                seed=self.seed

            ).generate_dataframe()

        )

        # ----------------------------------------
        # Validation
        # ----------------------------------------

        validator = DataValidator(

            customer_dataframe=customer_df,

            bureau_dataframe=bureau_df,

            card_dataframe=card_df,

            loan_dataframe=loan_df,

            transaction_dataframe=transaction_df,

            digital_behavior_dataframe=digital_df

        )

        if not validator.validate():

            validator.validation_summary()

            print()

            print(

                "Pipeline terminated "

                "due to validation errors."

            )

            return

        validator.validation_summary()

        # ----------------------------------------
        # Export
        # ----------------------------------------

        exporter = DataExporter()

        exported_files = (

            exporter.export_all(

                customer_dataframe=customer_df,

                bureau_dataframe=bureau_df,

                card_dataframe=card_df,

                loan_dataframe=loan_df,

                transaction_dataframe=transaction_df,

                digital_behavior_dataframe=digital_df

            )

        )

        exporter.export_summary(

            exported_files

        )

        # ----------------------------------------
        # Pipeline Summary
        # ----------------------------------------

        print()

        print("=" * 60)

        print(

            "PIPELINE COMPLETED SUCCESSFULLY"

        )

        print("=" * 60)

        print(

            f"Customers           : {len(customer_df)}"

        )

        print(

            f"Bureau Records      : {len(bureau_df)}"

        )

        print(

            f"Credit Cards        : {len(card_df)}"

        )

        print(

            f"Loan Accounts       : {len(loan_df)}"

        )

        print(

            f"Transactions        : {len(transaction_df)}"

        )

        print(

            f"Digital Sessions    : {len(digital_df)}"

        )

        print("=" * 60)


# ----------------------------------------
# Local Testing
# ----------------------------------------

if __name__ == "__main__":

    pipeline = CustomerDataPipeline()

    pipeline.run()
