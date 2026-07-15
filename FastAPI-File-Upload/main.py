from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import os
import shutil

app = FastAPI()

UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Allow only PDF and DOCX files
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_size = os.path.getsize(file_path)

    # Store metadata in PostgreSQL
    db: Session = SessionLocal()

    new_file = models.File(
        filename=file.filename,
        file_type=file.content_type,
        file_size=file_size,
        file_path=file_path
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    db.close()

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "file_size": file_size,
        "file_path": file_path
    }