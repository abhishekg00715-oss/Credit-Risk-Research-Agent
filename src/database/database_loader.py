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
        directory: str = OUTPUT_DIRECTORY
    ):

        self.database_name = database_name

        self.data_directory = Path(
            directory
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
    # Normalize DataFrame for Table
    # ----------------------------------------

    @staticmethod
    def normalize_dataframe_for_table(
        dataframe: pd.DataFrame,
        table_name: str
    ) -> pd.DataFrame:

        normalized_dataframe = dataframe.copy()

        if table_name == "credit_card_accounts":

            if (
                "available_limit" in normalized_dataframe.columns
                and "available_credit" not in normalized_dataframe.columns
            ):

                normalized_dataframe["available_credit"] = (
                    normalized_dataframe["available_limit"]
                )

            elif (
                "available_credit" in normalized_dataframe.columns
                and "available_limit" not in normalized_dataframe.columns
            ):

                normalized_dataframe["available_limit"] = (
                    normalized_dataframe["available_credit"]
                )

        if table_name == "loan_accounts":

            if (
                "sanctioned_amount" in normalized_dataframe.columns
                and "loan_amount" not in normalized_dataframe.columns
            ):

                normalized_dataframe["loan_amount"] = (
                    normalized_dataframe["sanctioned_amount"]
                )

            if (
                "monthly_emi" in normalized_dataframe.columns
                and "emi_amount" not in normalized_dataframe.columns
            ):

                normalized_dataframe["emi_amount"] = (
                    normalized_dataframe["monthly_emi"]
                )

            if (
                "secured" in normalized_dataframe.columns
                and "secured_flag" not in normalized_dataframe.columns
            ):

                normalized_dataframe["secured_flag"] = (
                    normalized_dataframe["secured"]
                )

        return normalized_dataframe

    # ----------------------------------------
    # Ensure Table Compatibility
    # ----------------------------------------

    def ensure_table_columns(
        self,
        table_name: str,
        dataframe: pd.DataFrame
    ):

        table_info = self.database.connection.execute(
            f"PRAGMA table_info({table_name})"
        ).fetchall()

        existing_columns = {
            column[1] for column in table_info
        }

        for column_name in dataframe.columns:

            if column_name in existing_columns:

                continue

            inferred_type = self.infer_sql_column_type(
                dataframe[column_name]
            )

            self.database.execute(
                f"ALTER TABLE {table_name} ADD COLUMN {column_name} {inferred_type};"
            )

        if table_name == "credit_card_accounts":

            if "available_credit" in dataframe.columns and "available_limit" in dataframe.columns:

                dataframe.loc[:, "available_credit"] = dataframe["available_credit"].fillna(dataframe["available_limit"])
                dataframe.loc[:, "available_limit"] = dataframe["available_limit"].fillna(dataframe["available_credit"])

    @staticmethod
    def infer_sql_column_type(series: pd.Series) -> str:

        if pd.api.types.is_bool_dtype(series):

            return "BOOLEAN"

        if pd.api.types.is_integer_dtype(series):

            return "INTEGER"

        if pd.api.types.is_float_dtype(series):

            return "REAL"

        numeric_series = pd.to_numeric(series.dropna(), errors="coerce")

        if numeric_series.notna().all():

            if (numeric_series % 1 == 0).all():

                return "INTEGER"

            return "REAL"

        return "TEXT"

    # ----------------------------------------
    # Load DataFrame
    # ----------------------------------------
  
    def load_dataframe(
        self,
        dataframe: pd.DataFrame,
        table_name: str
    ):
        print(table_name)

        print(dataframe.columns.tolist())

        print(dataframe.head(1))

        normalized_dataframe = self.normalize_dataframe_for_table(
            dataframe,
            table_name
        )

        self.ensure_table_columns(
            table_name,
            normalized_dataframe
        )

        normalized_dataframe.to_sql(

            table_name,

            self.database.connection,

            if_exists="append",

            index=False

        )

        self.loaded_records[table_name] = (

            len(normalized_dataframe)
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

        with self.database:
            
            self.database.create_schema()

            for table in tables_to_clear:

                self.database.execute(
            
                    f"DELETE FROM {table};"
            
                )

            for file_name, table_name in dataset_mapping:
                print(

                    f"Loading {table_name}..."
                
                )
                
                dataframe = self.read_csv(
                    file_name
                )
                
                self.load_dataframe(

                    dataframe,

                    table_name

                )
            self.database.commit()

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
