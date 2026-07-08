"""
digital_behavior_generator.py

Purpose:
Generate synthetic digital banking
behaviour for each customer.

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
    MIN_DIGITAL_SESSIONS,
    MAX_DIGITAL_SESSIONS,
    DEVICE_TYPES,
    LOGIN_CHANNELS
)


class DigitalBehaviorGenerator:
    """
    Generate synthetic digital
    banking behaviour.
    """

    def __init__(
        self,
        customer_dataframe: pd.DataFrame,
        transaction_dataframe: pd.DataFrame,
        seed: int = 42
    ):

        self.customer_dataframe = (
            customer_dataframe
        )

        self.transaction_dataframe = (
            transaction_dataframe
        )

        random.seed(seed)

    # ----------------------------------------
    # Session ID
    # ----------------------------------------

    @staticmethod
    def generate_session_id(
        session_number: int
    ) -> str:

        return (
            f"SESS{session_number:010d}"
        )

    # ----------------------------------------
    # Number of Sessions
    # ----------------------------------------

    @staticmethod
    def number_of_sessions(
        customer_segment: str
    ) -> int:
        """
        Higher value customers tend to
        engage more frequently through
        digital channels.
        """

        if customer_segment == (
            "High Net Worth"
        ):

            return random.randint(
                35,
                MAX_DIGITAL_SESSIONS
            )

        elif customer_segment == (
            "Affluent"
        ):

            return random.randint(
                20,
                35
            )

        return random.randint(
            MIN_DIGITAL_SESSIONS,
            20
        )

    # ----------------------------------------
    # Login Channel
    # ----------------------------------------

    @staticmethod
    def login_channel() -> str:

        return random.choices(

            LOGIN_CHANNELS,

            weights=[
                80,
                20
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Device Type
    # ----------------------------------------

    @staticmethod
    def device_type() -> str:

        return random.choices(

            DEVICE_TYPES,

            weights=[
                60,   # Android

                25,   # iPhone

                10,   # Windows

                5     # MacBook
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Login Status
    # ----------------------------------------

    @staticmethod
    def login_status() -> str:

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
    # Session Duration
    # ----------------------------------------

    @staticmethod
    def session_duration() -> int:
        """
        Duration in minutes.
        Most sessions are short.
        """

        return random.choices(

            [
                random.randint(2, 5),

                random.randint(6, 10),

                random.randint(11, 20)
            ],

            weights=[
                50,

                35,

                15
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Transactions Per Session
    # ----------------------------------------

    @staticmethod
    def transactions_per_session() -> int:
        """
        Most sessions are used
        for enquiries rather than
        financial transactions.
        """

        return random.choices(

            [
                0,

                1,

                2,

                3,

                4

            ],

            weights=[
                40,

                30,

                15,

                10,

                5
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Biometric Login
    # ----------------------------------------

    @staticmethod
    def biometric_login(
        device_type: str
    ) -> str:
        """
        Mobile devices are more
        likely to support biometric
        authentication.
        """

        if device_type == (
            "Android"
        ):

            probability = 70

        elif device_type == (
            "iPhone"
        ):

            probability = 90

        else:

            probability = 0

        return random.choices(

            [

                "Yes",

                "No"

            ],

            weights=[
                probability,

                100 - probability
            ],

            k=1

        )[0]

    # ----------------------------------------
    # Login DateTime
    # ----------------------------------------

    @staticmethod
    def login_datetime():
        """
        Generate a login timestamp
        within the previous year.
        """

        return (

            datetime.now()

            -

            timedelta(

                days=random.randint(
                    1,
                    365
                ),

                hours=random.randint(
                    0,
                    23
                ),

                minutes=random.randint(
                    0,
                    59
                )

            )

        )
