"""
schema.py

Purpose:
Contains all database schema definitions
for the Customer Risk Assessment module.

Author:
Credit Risk Research Agent
"""

# --------------------------------------------------
# Customer Master Table
# --------------------------------------------------

CREATE_CUSTOMER_MASTER_TABLE = """
CREATE TABLE IF NOT EXISTS customer_master (

    customer_id TEXT PRIMARY KEY,

    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,

    gender TEXT,
    date_of_birth TEXT,

    employment_type TEXT,
    occupation TEXT,

    annual_income REAL,

    city TEXT,
    state TEXT,

    customer_since TEXT,

    relationship_years INTEGER
);
"""


# --------------------------------------------------
# Credit Bureau Table
# --------------------------------------------------

CREATE_CREDIT_BUREAU_TABLE = """
CREATE TABLE IF NOT EXISTS credit_bureau (

    bureau_id INTEGER PRIMARY KEY AUTOINCREMENT,

    customer_id TEXT NOT NULL,

    credit_score INTEGER,
    credit_history_years INTEGER,

    hard_inquiries INTEGER,
    delinquencies INTEGER,
    defaults_count INTEGER,

    bankruptcy_flag INTEGER,

    credit_utilization REAL,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Credit Card Accounts Table
# --------------------------------------------------

CREATE_CREDIT_CARD_TABLE = """
CREATE TABLE IF NOT EXISTS credit_card_accounts (

    card_id TEXT PRIMARY KEY,

    customer_id TEXT NOT NULL,

    card_type TEXT,

    credit_limit REAL,

    outstanding_balance REAL,

    utilization_ratio REAL,

    payment_status TEXT,

    late_payments INTEGER,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Loan Accounts Table
# --------------------------------------------------

CREATE_LOAN_TABLE = """
CREATE TABLE IF NOT EXISTS loan_accounts (

    loan_id TEXT PRIMARY KEY,

    customer_id TEXT NOT NULL,

    loan_type TEXT,

    loan_amount REAL,

    outstanding_balance REAL,

    monthly_emi REAL,

    interest_rate REAL,

    loan_status TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Transactions Table
# --------------------------------------------------

CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (

    transaction_id TEXT PRIMARY KEY,

    customer_id TEXT NOT NULL,

    transaction_date TEXT,

    merchant_category TEXT,

    amount REAL,

    transaction_type TEXT,

    channel TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Digital Behavior Table
# --------------------------------------------------

CREATE_DIGITAL_BEHAVIOR_TABLE = """
CREATE TABLE IF NOT EXISTS digital_behavior (

    session_id TEXT PRIMARY KEY,

    customer_id TEXT NOT NULL,

    login_timestamp TEXT,

    device_type TEXT,

    channel TEXT,

    session_duration INTEGER,

    failed_login INTEGER,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Risk Assessment History
# --------------------------------------------------

CREATE_RISK_ASSESSMENT_HISTORY_TABLE = """
CREATE TABLE IF NOT EXISTS risk_assessment_history (

    assessment_id INTEGER
        PRIMARY KEY AUTOINCREMENT,

    customer_id TEXT NOT NULL,

    assessment_timestamp TEXT,

    overall_risk TEXT,

    recommended_product TEXT,

    llm_summary TEXT,

    confidence_score REAL,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Customer Features Table
# --------------------------------------------------

CREATE_CUSTOMER_FEATURES_TABLE = """
CREATE TABLE IF NOT EXISTS customer_features (

    customer_id TEXT PRIMARY KEY,

    debt_to_income_ratio REAL,

    credit_utilization REAL,

    repayment_score REAL,

    income_stability_score REAL,

    relationship_score REAL,

    financial_stress_score REAL,

    overall_risk_score REAL,

    last_updated TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customer_master(customer_id)
);
"""


# --------------------------------------------------
# Indexes
# --------------------------------------------------

CREATE_INDEXES = [

    """
    CREATE INDEX IF NOT EXISTS idx_bureau_customer
    ON credit_bureau(customer_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_card_customer
    ON credit_card_accounts(customer_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_loan_customer
    ON loan_accounts(customer_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_transaction_customer
    ON transactions(customer_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_transaction_date
    ON transactions(transaction_date);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_behavior_customer
    ON digital_behavior(customer_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_risk_customer
    ON risk_assessment_history(customer_id);
    """
]


# --------------------------------------------------
# Master Schema Collection
# --------------------------------------------------

ALL_TABLES = [

    CREATE_CUSTOMER_MASTER_TABLE,

    CREATE_CREDIT_BUREAU_TABLE,

    CREATE_CREDIT_CARD_TABLE,

    CREATE_LOAN_TABLE,

    CREATE_TRANSACTIONS_TABLE,

    CREATE_DIGITAL_BEHAVIOR_TABLE,

    CREATE_CUSTOMER_FEATURES_TABLE,

    CREATE_RISK_ASSESSMENT_HISTORY_TABLE
]
