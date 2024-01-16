from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    account_num = Column(Integer, primary_key=True)
    sort_code = Column(Integer, primary_key=True)
    user_id = Column(String)
    balance = Column(Integer)