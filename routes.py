from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/loans/')
async def get_loans(db: Session = Depends(get_db)):
    try:
        return await service.get_loans(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/loans/loan_id')
async def get_loans_loan_id(loan_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_loans_loan_id(db, loan_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/loans/')
async def post_loans(id: str, db: Session = Depends(get_db)):
    try:
        return await service.post_loans(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/loans/loan_id/')
async def put_loans_loan_id(raw_data: schemas.PutLoansLoanId, db: Session = Depends(get_db)):
    try:
        return await service.put_loans_loan_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/loans/loan_id')
async def delete_loans_loan_id(loan_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_loans_loan_id(db, loan_id)
    except Exception as e:
        raise HTTPException(500, str(e))

