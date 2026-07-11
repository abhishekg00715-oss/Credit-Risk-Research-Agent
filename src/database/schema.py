"""
schema.py

Purpose:
SQLite database schema definitions
for the Customer Risk Assessment
module.

Author:
Credit Risk Research Agent
"""

# ==================================================
# Customer Master
# ==================================================

CUSTOMER_MASTER_SCHEMA = """

CREATE TABLE IF NOT EXISTS customer_master (

    customer_id TEXT PRIMARY KEY,

    first_name TEXT,

    last_name TEXT,

    gender TEXT,

    date_of_birth DATE,

    employment_type TEXT,

    occupation TEXT,

    annual_income REAL,

    customer_segment TEXT,

    city TEXT,

    state TEXT,

    customer_since DATE,

    relationship_years INTEGER

);

"""


# ==================================================
# Credit Bureau
# ==================================================

CREDIT_BUREAU_SCHEMA = """

CREATE TABLE IF NOT EXISTS credit_bureau (

    customer_id TEXT PRIMARY KEY,

    credit_score INTEGER,

    bureau_rating TEXT,

    total_accounts INTEGER,

    active_accounts INTEGER,

    credit_utilization REAL,

    total_outstanding REAL,

    dti_ratio REAL,

    hard_inquiries INTEGER,

    late_payments INTEGER,

    defaults INTEGER,

    bankruptcies INTEGER,

    fraud_flag TEXT,

    last_bureau_refresh DATE,

    FOREIGN KEY(customer_id)

        REFERENCES customer_master(customer_id)

);

"""


# ==================================================
# Credit Card Accounts
# ==================================================

CREDIT_CARD_SCHEMA = """

CREATE TABLE IF NOT EXISTS credit_card_accounts (

    card_number TEXT PRIMARY KEY,

    customer_id TEXT,

    card_type TEXT,

    issue_date DATE,

    expiry_date DATE,

    credit_limit REAL,

    available_credit REAL,

    available_limit REAL,

    outstanding_balance REAL,

    utilization_percentage REAL,

    annual_fee REAL,

    cash_limit REAL,

    statement_balance REAL,

    billing_cycle_day INTEGER,

    minimum_due REAL,

    payment_due_date DATE,

    last_payment_amount REAL,

    last_payment_date DATE,

    payment_status TEXT,

    days_past_due INTEGER,

    missed_payments_last_12m INTEGER,

    write_off_flag TEXT,

    reward_program TEXT,

    reward_points INTEGER,

    last_card_transaction_date DATE,

    card_status TEXT,

    FOREIGN KEY(customer_id)

        REFERENCES customer_master(customer_id)

);

"""

# ==================================================
# Loan Accounts
# ==================================================

LOAN_SCHEMA = """

CREATE TABLE IF NOT EXISTS loan_accounts (

    loan_account_number TEXT PRIMARY KEY,

    customer_id TEXT,

    loan_type TEXT,

    loan_status TEXT,

    secured_flag TEXT,

    secured TEXT,

    loan_amount REAL,

    sanctioned_amount REAL,

    outstanding_balance REAL,

    interest_rate REAL,

    tenure_months INTEGER,

    remaining_tenure INTEGER,

    emi_amount REAL,

    monthly_emi REAL,

    repayment_status TEXT,

    days_past_due INTEGER,

    disbursement_date DATE,

    maturity_date DATE,

    FOREIGN KEY(customer_id)

        REFERENCES customer_master(customer_id)

);

"""


# ==================================================
# Transactions
# ==================================================

TRANSACTION_SCHEMA = """

CREATE TABLE IF NOT EXISTS transactions (

    transaction_id TEXT PRIMARY KEY,

    customer_id TEXT,

    transaction_date DATE,

    transaction_type TEXT,

    merchant_category TEXT,

    transaction_channel TEXT,

    transaction_amount REAL,

    debit_credit_indicator TEXT,

    account_type TEXT,

    FOREIGN KEY(customer_id)

        REFERENCES customer_master(customer_id)

);

"""


# ==================================================
# Digital Behaviour
# ==================================================

DIGITAL_BEHAVIOR_SCHEMA = """

CREATE TABLE IF NOT EXISTS digital_behavior (

    session_id TEXT PRIMARY KEY,

    customer_id TEXT,

    login_timestamp DATETIME,

    login_channel TEXT,

    device_type TEXT,

    login_status TEXT,

    activity_type TEXT,

    session_duration_minutes INTEGER,

    transactions_in_session INTEGER,

    biometric_login TEXT,

    FOREIGN KEY(customer_id)

        REFERENCES customer_master(customer_id)

);

"""


# ==================================================
# Database Schema
# ==================================================


DATABASE_SCHEMA = [

    CUSTOMER_MASTER_SCHEMA,

    CREDIT_BUREAU_SCHEMA,

    CREDIT_CARD_SCHEMA,

    LOAN_SCHEMA,

    TRANSACTION_SCHEMA,

    DIGITAL_BEHAVIOR_SCHEMA

]


# --------------------------------------------------
# Local Testing
# --------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 50)

    print("Customer Risk Database Schema")

    print("=" * 50)

    print(

        f"Total Tables : {len(DATABASE_SCHEMA)}"

    )

    print()

    print(

        "customer_master"

    )

    print(

        "credit_bureau"

    )

    print(

        "credit_card_accounts"

    )

    print(

        "loan_accounts"

    )

    print(

        "transactions"

    )

    print(

        "digital_behavior"

    )
