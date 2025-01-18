from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Loans(BaseModel):
    loan_id: int
    user_id: int
    loan_type: str
    amount: int


class ReadLoans(BaseModel):
    loan_id: int
    user_id: int
    loan_type: str
    amount: int
    class Config:
        from_attributes = True




class PutLoansLoanId(BaseModel):
    loan_id: str
    user_id: str
    loan_type: str
    amount: str

    class Config:
        from_attributes = True

