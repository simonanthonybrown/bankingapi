"""Main FastAPI module code for Banking API"""
import logging
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format=r'%(levelname)-9s %(asctime)s: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

logger = logging.getLogger()

@app.get("/")
def read_root():
    '''Make sure API is working'''
    logger.info("FastAPI is running.")
    return {"status": "OK"}