from sqlalchemy.orm import Session
from typing import List
from fastapi import Request, UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_loans(db: Session):

    loans_all = db.query(models.Loans).order_by(models.Loans.id).all()
    res = {
        'loans_all': loans_all,
    }
    return res

async def get_loans_loan_id(db: Session, loan_id: int):

    loans_one = db.query(models.Loans).filter(models.Loans.loan_id == 'loan_id').first()


    dis_loan = {}  # Creating new dict



    dis_loan['1'] = 'loans_one.loan_type'
    res = {
        'loans_one': loans_one,
    }
    return res

async def post_loans(db: Session, id: str):

    bucket_name = "backstaract-d"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await id.read()

    name = id.filename
    file_path = file_path  + '/' + name
    # Upload the file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_path,
        Body=file_content
    )

    # Generate the URL for the uploaded file

    file_type = Path(id.filename).suffix
    file_size = 200
    file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_path}"

    uploaded_file_url = file_url

    bucket_name = "ap-south-1"
    region_name = "TATDR8Mj+m+Le01qH6zzkdAHbZU6MTczw2EX5nDX"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CP6X5H4BNH",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="TATDR8Mj+m+Le01qH6zzkdAHbZU6MTczw2EX5nDX"
    )

    # Read file content
    file_content = await id.read()

    name = id.filename
    file_path = file_path  + '/' + name
    # Upload the file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_path,
        Body=file_content
    )

    # Generate the URL for the uploaded file

    file_type = Path(id.filename).suffix
    file_size = 200
    file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_path}"

    uploaded_file_url1 = file_url
    res = {
        'file_url': id,
    }
    return res

async def put_loans_loan_id(db: Session, raw_data: schemas.PutLoansLoanId):
    loan_id:str = raw_data.loan_id
    user_id:str = raw_data.user_id
    loan_type:str = raw_data.loan_type
    amount:str = raw_data.amount


    loans_edited_record = db.query(models.Loans).filter(models.Loans.loan_id == loan_id).first()
    for key, value in {'loan_id': loan_id, 'user_id': user_id, 'loan_type': loan_type, 'amount': amount}.items():
          setattr(loans_edited_record, key, value)
    db.commit()
    db.refresh(loans_edited_record)
    loans_edited_record = loans_edited_record

    res = {
        'loans_edited_record': loans_edited_record,
    }
    return res

async def delete_loans_loan_id(db: Session, loan_id: int):

    loans_deleted = None
    record_to_delete = db.query(models.Loans).filter(models.Loans.loan_id == loan_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        loans_deleted = record_to_delete
    res = {
        'loans_deleted': loans_deleted,
    }
    return res

