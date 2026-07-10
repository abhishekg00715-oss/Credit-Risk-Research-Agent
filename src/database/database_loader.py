"""
database_loader.py

Purpose:
Load exported CSV datasets
into the SQLite database.

Author:
Credit Risk Research Agent
"""

from pathlib import Path

import pandas as pd

from src.database.database_utils import (
    DatabaseManager
)

from src.database.customer_data_generator.config import (

    OUTPUT_DIRECTORY,

    CUSTOMER_MASTER_FILE,

    CREDIT_BUREAU_FILE,

    CREDIT_CARD_FILE,

    LOAN_FILE,

    TRANSACTION_FILE,

    DIGITAL_BEHAVIOR_FILE

)


class DatabaseLoader:
    """
    Load exported CSV files
    into SQLite.
    """

    def __init__(
        self,
        database_name: str = "customer_risk.db",
        data_directory=OUTPUT_DIRECTORY
    ):

        self.database_name = database_name

        self.data_directory = Path(
            data_directory
        )

        self.database = DatabaseManager(
            database_name
        )

        self.loaded_records = {}


    # ----------------------------------------
    # Read CSV
    # ----------------------------------------

    def read_csv(
        self,
        file_name: str
    ) -> pd.DataFrame:

        file_path = (

            self.data_directory

            / file_name

        )

        return pd.read_csv(
            file_path
        )

      # ----------------------------------------
    # Load DataFrame
    # ----------------------------------------

    def load_dataframe(
        self,
        dataframe: pd.DataFrame,
        table_name: str
    ):

        dataframe.to_sql(

            table_name,

            self.database.connection,

            if_exists="append",

            index=False

        )

        self.loaded_records[table_name] = (

            len(dataframe)
        )

    # ----------------------------------------
    # Load All Datasets
    # ----------------------------------------

    def load_all(
        self
    ):

        dataset_mapping = [

            (
                CUSTOMER_MASTER_FILE,
                "customer_master"
            ),

            (
                CREDIT_BUREAU_FILE,
                "credit_bureau"
            ),

            (
                CREDIT_CARD_FILE,
                "credit_card_accounts"
            ),

            (
                LOAN_FILE,
                "loan_accounts"
            ),

            (
                TRANSACTION_FILE,
                "transactions"
            ),

            (
                DIGITAL_BEHAVIOR_FILE,
                "digital_behavior"
            )

        ]

        tables_to_clear = [

            "digital_behavior",
        
            "transactions",
        
            "loan_accounts",
        
            "credit_card_accounts",
        
            "credit_bureau",
        
            "customer_master"
        
        ]

       for table in tables_to_clear:

        self.database.execute(
    
            f"DELETE FROM {table};"
    
        )

            self.database.create_schema()

            for file_name, table_name in dataset_mapping:

                dataframe = self.read_csv(
                    file_name
                )
                
                self.load_dataframe(

                    dataframe,

                    table_name

                )

    # ----------------------------------------
    # Loading Summary
    # ----------------------------------------

    def loading_summary(
        self
    ):

        print()

        print("=" * 60)

        print("DATABASE LOADING SUMMARY")

        print("=" * 60)

        for table_name, row_count in (

            self.loaded_records.items()

        ):

            print(

                f"{table_name:<25}"

                f"{row_count:>8} rows"

            )

        print("=" * 60)

    # ----------------------------------------
    # Execute Loader
    # ----------------------------------------

    def run(
        self
    ):

        print()

        print("=" * 60)

        print(

            "LOADING CSV DATA INTO SQLITE"

        )

        print("=" * 60)

        self.load_all()

        self.loading_summary()

        print()

        print("=" * 60)

        print(

            "DATABASE LOAD COMPLETED"

        )

        print("=" * 60)


# --------------------------------------------------
# Local Testing
# --------------------------------------------------

if __name__ == "__main__":

    loader = DatabaseLoader()

    loader.run()

        )

  
