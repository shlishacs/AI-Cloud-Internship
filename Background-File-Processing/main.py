from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import os
import shutil
import time

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Background task
def process_file(filename: str):
    print(f"Processing {filename}...")
    time.sleep(5)   # Simulates processing
    print(f"{filename} processed successfully!")

# Upload endpoint
@app.post("/upload")
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run background task
    background_tasks.add_task(process_file, file.filename)

    return {
        "message": "File uploaded successfully. Background processing started.",
        "filename": file.filename
    }