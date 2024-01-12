"""Main FastAPI module code for Banking API"""
import logging
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Account
from fastapi import FastAPI

# Enable logging for the file
logging.basicConfig(
    level=logging.INFO,
    format=r'%(levelname)-9s %(asctime)s: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

# Create instance of logger for use in path operations
logger = logging.getLogger()

# Define the FastAPI app
app = FastAPI()

# Route to check that FastAPI is running on Uvicorn boot
@app.get("/")
def read_root():
    '''Make sure API is working'''
    logger.info("FastAPI is running.")
    return {"status": "OK"}


# Route to retrieve account balance
@app.get("/{account_num}/{sort_code}")
def fetch_balance(account_num: int, sort_code: int):
    '''Check for account number and sort code in db, return balance
    if account exists'''
    
    # Connect to the database using SQLAlchemy
    engine = create_engine(f"sqlite:///banking.db")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    statement = (
        select(Account.balance)
        .where(Account.account_num == account_num)
        .where(Account.sort_code == sort_code)
    )

    account_balance = session.scalars(statement).all()

    return account_balance
