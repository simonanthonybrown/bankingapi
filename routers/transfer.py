import logging
from fastapi import APIRouter, HTTPException
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
    prefix="/transfer"
)

@router.get("/{origin_acc}/{origin_sort}/{dest_acc}/{dest_sort}/{amount}")
def transfer_funds(origin_acc: int, origin_sort:int, dest_acc: int, dest_sort: int, amount: int):
    '''Remove funds from origin account and add them to the destination account'''
    
    logger.info("Checking origin and destination account details...")

    # Connect to the database using SQLAlchemy
    engine = create_engine(f"sqlite:///banking.db")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # SQL statement using the SQLAlchemy account model set up in models.py
    origin_statement = (
        select(Account.balance)
        .where(Account.account_num == origin_acc)
        .where(Account.sort_code == origin_sort)
    )

    origin_balance = session.scalars(origin_statement).all()

    # If origin balance list is empty then account is not in the DB
    if len(origin_balance) == 0:
        raise HTTPException(
            status_code=404,
            detail="Error 404: Origin account not found, please double check account number and sort code."
        )

    print(f"Origin balance before: {origin_balance[0]}")

    # SQL statement for destination account details
    dest_statement = (
        select(Account.balance)
        .where(Account.account_num == dest_acc)
        .where(Account.sort_code == dest_sort)
    )

    dest_balance = session.scalars(dest_statement).all()

    # If origin balance list is empty then account is not in the DB
    if len(dest_balance) == 0:
        raise HTTPException(
            status_code=404,
            detail="Error 404: Destination account not found, please double check account number and sort code."
        )

    print(f"Dest balance before: {dest_balance[0]}")

    logger.info("Transferring funds...")

    # Calculate the differences to both accounts
    origin_remaining = origin_balance[0] - amount
    dest_total = dest_balance[0] + amount

    # Update the changes to the account balance values
    session.query(Account).filter(Account.account_num == origin_acc).filter(Account.sort_code == origin_sort).update({Account.balance: origin_remaining})
    session.query(Account).filter(Account.account_num == dest_acc).filter(Account.sort_code == dest_sort).update({Account.balance: dest_total})
    
    session.commit()

    origin_post_trans = (
        select(Account.balance)
        .where(Account.account_num == origin_acc)
        .where(Account.sort_code == origin_sort)
    )

    second_origin_balance = session.scalars(origin_post_trans).all()

    dest_post_trans = (
    select(Account.balance)
    .where(Account.account_num == dest_acc)
    .where(Account.sort_code == dest_sort)
    )

    seconds_dest_balance = session.scalars(dest_post_trans).all()

    print(f"Post transfer balance in origin account: {second_origin_balance[0]}")
    print(f"Post transfer balance in destination account: {seconds_dest_balance[0]}")

    return "Transfer complete"