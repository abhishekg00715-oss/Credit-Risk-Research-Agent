"""
customer_generator.py

Purpose:
Generate synthetic customer master data
for the Credit Risk Research Agent.

Author:
Credit Risk Research Agent
"""

import random
import uuid

import pandas as pd

from faker import Faker
from datetime import datetime
from src.database.customer_data_generator.config import (
    EMPLOYMENT_TYPES,
    OCCUPATION_MAPPING,
    SALARIED_INCOME,
    SELF_EMPLOYED_INCOME,
    BUSINESS_OWNER_INCOME,
)


class CustomerGenerator:
    """
    Generates synthetic customer
    master records.
    """

    def __init__(
        self,
        number_of_customers: int = 100,
        seed: int = 42
    ):

        self.number_of_customers = (
            number_of_customers
        )

        self.fake = Faker()

        Faker.seed(seed)

        random.seed(seed)

        self.fake.unique.clear()

        self.current_year = (
            datetime.now().year
        )

        
        

    # --------------------------------------------------
    # Customer ID
    # --------------------------------------------------

    def generate_customer_id(
        self,
        customer_number: int
    ) -> str:

        return (
            f"CUST{customer_number:06d}"
        )

    # --------------------------------------------------
    # Employment Type
    # --------------------------------------------------

    def generate_employment_type(
        self
    ):

        return random.choice(
            EMPLOYMENT_TYPES
        )

    # --------------------------------------------------
    # Annual Income
    # --------------------------------------------------

    def generate_income(
        self,
        employment_type: str
    ) -> float:

        if employment_type == "Business Owner":

            return random.randint(
              BUSINESS_OWNER_INCOME[0],
              BUSINESS_OWNER_INCOME[1]
            )

        elif employment_type == "Self-Employed":

            return random.randint(
                SELF_EMPLOYED_INCOME[0],
                SELF_EMPLOYED_INCOME[1]
            )

        return random.randint(
            SALARIED_INCOME[0],
            SALARIED_INCOME[1]
        )
        
    # --------------------------------------------------
    # Customer Segment
    # --------------------------------------------------
    
    def determine_customer_segment(
        self,
        income: float
    ):

        if income >= 2500000:
    
            return "High Net Worth"
    
        elif income >= 1200000:
    
            return "Affluent"
    
        return "Mass"
    
    
    # --------------------------------------------------
    # Relationship Years
    # --------------------------------------------------

    def generate_relationship_years(
        self
    ):

        return random.randint(
            1,
            20
        )

    # --------------------------------------------------
    # Customer Since
    # --------------------------------------------------

    def customer_since(
        self,
        relationship_years: int
    ):

        return (
            f"{self.current_year - relationship_years}"
            "-01-01"
        )

    # --------------------------------------------------
    # Generate One Customer
    # --------------------------------------------------

    def generate_customer(
        self,customer_number: int
    ):

        employment = (
            self.generate_employment_type()
        )

        relationship = (
            self.generate_relationship_years()
        )

        income = (
            self.generate_income(
                employment
            )
        )

        customer_segment = (
            self.determine_customer_segment(
                income
            )
        )
        return {

            "customer_id":
                self.generate_customer_id(customer_number),

            "first_name":
                self.fake.first_name(),

            "last_name":
                self.fake.last_name(),

            "gender":
                random.choice(
                    [
                        "Male",
                        "Female"
                    ]
                ),

            "date_of_birth":
                self.fake.date_of_birth(
                    minimum_age=21,
                    maximum_age=65
                ).isoformat(),

            "employment_type":
                employment,

            "occupation":
                random.choice(
                     OCCUPATION_MAPPING[
                        employment
                     ]
                ),

            "annual_income":
                income,
            "customer_segment":
                customer_segment,                
            "city":
                self.fake.city(),

            "state":
                self.fake.state(),

            "customer_since":
                self.customer_since(
                    relationship
                ),

            "relationship_years":
                relationship
        }

    # --------------------------------------------------
    # Generate DataFrame
    # --------------------------------------------------

    def generate_dataframe(
        self
    ) -> pd.DataFrame:

        customers = [

            self.generate_customer(customer_number)

            for customer_number in range(
                1,
                self.number_of_customers + 1
            )

        ]

        dataframe = pd.DataFrame(
            customers
        )

        return dataframe


# --------------------------------------------------
# Local Testing
# --------------------------------------------------

if __name__ == "__main__":

    generator = CustomerGenerator(
        number_of_customers=10
    )

    df = generator.generate_dataframe()

    print(df.head())

    print()

    print(df.info())
