import pandas as pd

from src.database.database_loader import DatabaseLoader


def test_normalize_dataframe_for_credit_card_table_maps_available_limit():
    dataframe = pd.DataFrame(
        [{"available_limit": 1500.0, "credit_limit": 2000.0}]
    )

    normalized = DatabaseLoader.normalize_dataframe_for_table(
        dataframe,
        "credit_card_accounts",
    )

    assert "available_credit" in normalized.columns
    assert "available_limit" in normalized.columns
    assert normalized.loc[0, "available_credit"] == 1500.0
    assert normalized.loc[0, "available_limit"] == 1500.0
