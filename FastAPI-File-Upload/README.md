# FastAPI File Upload API

## Overview

The FastAPI File Upload API is a RESTful web application developed using FastAPI that allows users to upload PDF and DOCX files. Uploaded files are stored locally in the `uploads` folder, while their metadata is stored in a PostgreSQL database using SQLAlchemy.

## Features

- Upload PDF and DOCX files
- Validate supported file types
- Store uploaded files locally
- Save file metadata in PostgreSQL
- Interactive API documentation with Swagger UI
- SQLAlchemy ORM integration

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- python-dotenv
- python-multipart

## Project Structure

```
fastapi-file-upload-api/
│
├── uploads/
├── main.py
├── database.py
├── models.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-file-upload-api.git
cd fastapi-file-upload-api
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration

Create a PostgreSQL database named:

```
file_upload_db
```

Create a `.env` file and add:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/file_upload_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

## Run the Application

```bash
uvicorn main:app --reload
```

Open the application:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

### Upload File

**POST** `/upload`

Accepts:

- PDF (.pdf)
- DOCX (.docx)

### Sample Response

```json
{
  "message": "File uploaded successfully",
  "filename": "resume.pdf",
  "file_size": 67143,
  "file_path": "uploads/resume.pdf"
}
```

## Database Schema

The application stores the following metadata in PostgreSQL:

- File Name
- File Type
- File Size
- File Path
- Upload Timestamp

## Future Enhancements

- Unique file naming using UUID
- File deletion endpoint
- Retrieve uploaded file details
- User authentication and authorization
- Cloud storage integration (AWS S3 or Azure Blob Storage)

## Author

**Shlisha C S**

MCA (Cloud Computing)
