"""
exporter.py

Purpose:
Export generated datasets
to CSV files.

Author:
Credit Risk Research Agent
"""

from pathlib import Path

import pandas as pd

from src.database.customer_data_generator.config import (

    OUTPUT_DIRECTORY,

    CUSTOMER_MASTER_FILE,

    CREDIT_BUREAU_FILE,

    CREDIT_CARD_FILE,

    LOAN_FILE,

    TRANSACTION_FILE,

    DIGITAL_BEHAVIOR_FILE

)


class DataExporter:
    """
    Export generated datasets
    as CSV files.
    """

    def __init__(
        self,
        output_directory: str = OUTPUT_DIRECTORY
    ):

        self.output_directory = Path(
            output_directory
        )

        self.output_directory.mkdir(

            parents=True,

            exist_ok=True

        )

    # ----------------------------------------
    # Export Single DataFrame
    # ----------------------------------------

    def export_dataframe(
        self,
        dataframe: pd.DataFrame,
        file_name: str
    ):

        output_file = (

            self.output_directory

            / file_name

        )

        dataframe.to_csv(

            output_file,

            index=False

        )

        return output_file


    # ----------------------------------------
    # Export All DataFrames
    # ----------------------------------------

    def export_all(
        self,
        customer_dataframe: pd.DataFrame,
        bureau_dataframe: pd.DataFrame,
        card_dataframe: pd.DataFrame,
        loan_dataframe: pd.DataFrame,
        transaction_dataframe: pd.DataFrame,
        digital_behavior_dataframe: pd.DataFrame
    ):

        exported_files = {}

        exported_files["Customer Master"] = (

            self.export_dataframe(

                customer_dataframe,

                CUSTOMER_MASTER_FILE

            )

        )

        exported_files["Credit Bureau"] = (

            self.export_dataframe(

                bureau_dataframe,

                CREDIT_BUREAU_FILE

            )

        )

        exported_files["Credit Cards"] = (

            self.export_dataframe(

                card_dataframe,

                CREDIT_CARD_FILE

            )

        )

        exported_files["Loans"] = (

            self.export_dataframe(

                loan_dataframe,

                LOAN_FILE

            )

        )

        exported_files["Transactions"] = (

            self.export_dataframe(

                transaction_dataframe,

                TRANSACTION_FILE

            )

        )

        exported_files["Digital Behaviour"] = (

            self.export_dataframe(

                digital_behavior_dataframe,

                DIGITAL_BEHAVIOR_FILE

            )

        )

        return exported_files

    # ----------------------------------------
    # Export Summary
    # ----------------------------------------

    @staticmethod
    def export_summary(
        exported_files: dict
    ):

        print()

        print("=" * 60)

        print("DATA EXPORT SUMMARY")

        print("=" * 60)

        for dataset, file_path in (

            exported_files.items()

        ):

            print(

                f"{dataset:<22}"

                f" -> "

                f"{file_path}"

            )

        print("=" * 60)

    # ----------------------------------------
    # Local Testing
    # ----------------------------------------

if __name__ == "__main__":

    print(

        "Run through "

        "data_pipeline_execution.py"

    )
