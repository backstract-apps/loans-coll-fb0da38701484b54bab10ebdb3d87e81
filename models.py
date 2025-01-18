from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Loans(Base):
    __tablename__ = 'loans'
    loan_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=False)
    loan_type = Column(String, primary_key=False)
    amount = Column(Integer, primary_key=False)

