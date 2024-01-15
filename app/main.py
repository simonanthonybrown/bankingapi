"""Main FastAPI module code for Banking API"""
import logging
from fastapi import FastAPI
from app.routers import balance, transfer

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

# Call in routers for the module
app.include_router(balance.router)
app.include_router(transfer.router)

# Route to check that FastAPI is running on Uvicorn boot
@app.get("/")
def read_root():
    '''Make sure API is working'''
    logger.info("FastAPI is running.")
    return {"status": "OK"}
