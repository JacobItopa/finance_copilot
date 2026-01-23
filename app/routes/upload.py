from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.classifier import classify_transaction
import os
from app.services.parser import parse_csv
from app.services.storage import save_transactions


router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        transactions = parse_csv(file_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    classified_transactions = [
        classify_transaction(tx) for tx in transactions
    ]

    save_transactions(classified_transactions)

    return {
        "message": "File uploaded and categorized successfully",
        "transaction_count": len(classified_transactions),
        "sample_transaction": classified_transactions[0]
    }

