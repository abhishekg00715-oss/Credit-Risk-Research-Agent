"""
config.py

Purpose:
Central configuration and master reference
data for the Synthetic Customer Data Generator.

Author:
Credit Risk Research Agent
"""

# ==================================================
# General Configuration
# ==================================================

RANDOM_SEED = 42

NUMBER_OF_CUSTOMERS = 100

MAX_CREDIT_CARDS = 3

MAX_LOANS = 2

MIN_TRANSACTIONS = 40

MAX_TRANSACTIONS = 120

MIN_DIGITAL_SESSIONS = 10

MAX_DIGITAL_SESSIONS = 50


# ==================================================
# Customer Demographics
# ==================================================

GENDERS = [

    "Male",

    "Female"

]

MARITAL_STATUS = [

    "Single",

    "Married"

]

EMPLOYMENT_TYPES = [

    "Salaried",

    "Self-Employed",

    "Business Owner"

]

CUSTOMER_SEGMENTS = [

    "Mass",

    "Affluent",

    "High Net Worth"

]

EDUCATION_LEVELS = [

    "Graduate",

    "Post Graduate",

    "Professional",

    "Doctorate"

]

RESIDENTIAL_STATUS = [

    "Owned",

    "Rented"

]


# ==================================================
# Occupations
# ==================================================
OCCUPATION_MAPPING = {

    "Salaried": [

        "Software Engineer",
        "Teacher",
        "Doctor",
        "Marketing Manager",
        "Sales Executive",
        "Government Employee",
        "Data Scientist",
        "Consultant"
    ],

    "Self-Employed": [

        "Chartered Accountant",
        "Lawyer",
        "Architect",
        "Freelancer",
        "Consultant"
    ],

    "Business Owner": [

        "Retail Business Owner",
        "Restaurant Owner",
        "Manufacturing Owner",
        "Startup Founder",
        "Exporter"
    ]
}


# ==================================================
# Income Bands (Annual)
# ==================================================

SALARIED_INCOME = (

    400000,

    2500000

)

SELF_EMPLOYED_INCOME = (

    700000,

    3500000

)

BUSINESS_OWNER_INCOME = (

    1200000,

    5000000

)


# ==================================================
# Credit Score Bands
# ==================================================

POOR_SCORE = (

    600,

    649

)

FAIR_SCORE = (

    650,

    699

)

GOOD_SCORE = (

    700,

    749

)

VERY_GOOD_SCORE = (

    750,

    799

)

EXCELLENT_SCORE = (

    800,

    850

)


# ==================================================
# Banking Products
# ==================================================

CARD_PRODUCTS = {
    "Classic": {
        "min_score": 650,
        "income_multiplier": 0.25,
        "annual_fee": 500
    },
    "Gold": {
        "min_score": 700,
        "income_multiplier": 0.40,
        "annual_fee": 1500
    },
    "Platinum": {
        "min_score": 750,
        "income_multiplier": 0.60,
        "annual_fee": 5000
    },
    "Premium": {
        "min_score": 800,
        "income_multiplier": 0.80,
        "annual_fee": 10000
    }
}

LOAN_TYPES = [

    "Personal Loan",

    "Home Loan",

    "Vehicle Loan",

    "Education Loan"

]


# ==================================================
# Loan Status
# ==================================================

LOAN_STATUS = [

    "Active",

    "Closed"

]


# ==================================================
# Payment Status
# ==================================================

PAYMENT_STATUS = [

    "On Time",

    "Delayed"

]


# ==================================================
# Transaction Categories
# ==================================================

MERCHANT_CATEGORIES = [

    "Groceries",

    "Fuel",

    "Restaurant",

    "Shopping",

    "Travel",

    "Healthcare",

    "Utilities",

    "Insurance",

    "Education",

    "Entertainment",

    "Investment"

]


# ==================================================
# Transaction Channels
# ==================================================

TRANSACTION_CHANNELS = [

    "UPI",

    "POS",

    "ATM",

    "Internet Banking",

    "Mobile Banking"

]


# ==================================================
# Digital Banking
# ==================================================

DEVICE_TYPES = [

    "Android",

    "iPhone",

    "Windows",

    "MacBook"

]

LOGIN_CHANNELS = [

    "Mobile App",

    "Web Portal"

]


# ==================================================
# Geographic Distribution
# ==================================================

INDIAN_STATES = [

    "Karnataka",

    "Maharashtra",

    "Delhi",

    "Tamil Nadu",

    "Telangana",

    "Gujarat",

    "West Bengal",

    "Rajasthan"

]


# --------------------------------------------------
# Card Reward Programs
# --------------------------------------------------

REWARD_PROGRAMS = {

    "Classic": "Cashback",

    "Gold": "Reward Points",

    "Platinum": "Travel Rewards",

    "Premium": "Premium Lifestyle"

}


# --------------------------------------------------
# Billing Cycle
# --------------------------------------------------

BILLING_CYCLE_DAYS = [

    5,
    10,
    15,
    20,
    25
]



# ==================================================
# Business Thresholds
# ==================================================

PREMIUM_CARD_MIN_SCORE = 750

STANDARD_CARD_MIN_SCORE = 700

LOW_RISK_UTILIZATION = 30

MODERATE_RISK_UTILIZATION = 50

HIGH_RISK_UTILIZATION = 75

STANDARD_DTI_LIMIT = 40

PREMIUM_DTI_LIMIT = 35


# ==================================================
# Export Configuration
# ==================================================

OUTPUT_DIRECTORY = "output"

CUSTOMER_MASTER_FILE = "customer_master.csv"

CREDIT_BUREAU_FILE = "credit_bureau.csv"

CREDIT_CARD_FILE = "credit_card_accounts.csv"

LOAN_FILE = "loan_accounts.csv"

TRANSACTION_FILE = "transactions.csv"

DIGITAL_BEHAVIOR_FILE = "digital_behavior.csv"
