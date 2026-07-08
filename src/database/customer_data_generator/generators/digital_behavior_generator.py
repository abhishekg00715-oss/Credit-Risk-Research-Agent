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
    LOGIN_CHANNELS,
    DIGITAL_SESSION_TYPES
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

    # ----------------------------------------
    # Session type
    # ----------------------------------------

    @staticmethod
    def activity_type():
    
        return random.choices(
    
            list(DIGITAL_SESSION_TYPES.keys()),
    
            weights=list(DIGITAL_SESSION_TYPES.values()),
    
            k=1
    
        )[0]

    
    # ----------------------------------------
    # Maximum Transactions by Activity
    # ----------------------------------------
    
    @staticmethod
    def max_transactions_for_activity(
        activity_type: str
    ) -> int:
        """
        Maximum financial transactions
        expected for the activity.
        """
    
        mapping = {
    
            "Balance Enquiry": 0,
    
            "Statement Download": 0,
    
            "Offer Browsing": 0,
    
            "Profile Update": 0,
    
            "Loan Account View": 0,
    
            "Funds Transfer": 2,
    
            "Bill Payment": 1,
    
            "Credit Card Payment": 1,
    
            "Reward Redemption": 1,
    
            "Service Request": 0
    
        }
    
        return mapping.get(
            activity_type,
            0
        )

    
    # ----------------------------------------
    # Generate DataFrame
    # ----------------------------------------

    def generate_dataframe(
        self
    ) -> pd.DataFrame:

        digital_records = []

        session_number = 1

        # ------------------------------------
        # Transaction Count Lookup
        # ------------------------------------

        transaction_lookup = (

            self.transaction_dataframe

            .groupby("customer_id")

            .size()

            .to_dict()

        )

        # ------------------------------------
        # Generate Sessions
        # ------------------------------------

        for _, customer in (

            self.customer_dataframe.iterrows()

        ):

            customer_id = (
                customer["customer_id"]
            )

            customer_segment = (
                customer["customer_segment"]
            )

            customer_state = (
                customer["state"]
            )

            total_sessions = (

                self.number_of_sessions(
                    customer_segment
                )

            )

            total_transactions = (

                transaction_lookup.get(
                    customer_id,
                    0
                )

            )

            remaining_transactions = (
                total_transactions
            )

            for session in range(
                total_sessions
            ):

                device = (
                    self.device_type()
                )

        # ------------------------------------
        # Allocate Transactions
        # ------------------------------------

                
                login_status = self.login_status()
                
                if login_status == "Failed":
                
                    activity_type = "Login Failed"
                
                    session_transactions = 0
                
                else:
                
                    activity_type = self.activity_type()
                
                    max_transactions = (
                        self.max_transactions_for_activity(
                            activity_type
                        )
                    )
                
                    if remaining_transactions <= 0:
                
                        session_transactions = 0
                
                    elif session == total_sessions - 1:
                
                        session_transactions = min(
                
                            remaining_transactions,
                
                            max_transactions
                
                        )
                
                    else:
                
                        session_transactions = random.randint(
                
                            0,
                
                            min(
                
                                max_transactions,
                
                                remaining_transactions
                
                            )
                
                        )
                
                if session_transactions > 0:
                
                    remaining_transactions -= session_transactions
                

                digital_records.append(

                    {

                        "session_id":
                            self.generate_session_id(
                                session_number
                            ),

                        "customer_id":
                            customer_id,

                        "login_datetime":
                            self.login_datetime(),

                        "login_channel":
                            self.login_channel(),

                        "device_type":
                            device,

                        "login_status":
                            login_status,

                        "session_duration_minutes":
                            self.session_duration(),

                        "activity_type": activity_type,
                        
                        "transactions_in_session":
                            session_transactions,

                        "biometric_login":
                            self.biometric_login(
                                device
                            ),

                        "state":
                            customer_state

                    }

                )

                session_number += 1

        return pd.DataFrame(
            digital_records
        )


# ----------------------------------------
# Local Testing
# ----------------------------------------

if __name__ == "__main__":

    print(
        "Run through data_pipeline_execution.py"
    )
