import logging
from fastapi import APIRouter
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Account

# Set up formatting for logging
logging.basicConfig(
    level=logging.INFO,
    format=r'%(levelname)-9s %(asctime)s: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

# Call the logger
logger = logging.getLogger()

# Set up a prefix for all HTML paths in this router
router = APIRouter(
    prefix="/balance"
)

# Route to retrieve account balance
@router.get("/{account_num}/{sort_code}")
def fetch_balance(account_num: int, sort_code: int):
    '''Check for account number and sort code in db, return balance
    if account exists'''
    
    logger.info("Checking for current account balance...")

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

    return f'Balance available: £{account_balance[0]}'