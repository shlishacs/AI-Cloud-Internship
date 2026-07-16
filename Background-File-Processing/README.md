# Background File Processing

## Overview

This project demonstrates asynchronous file processing using FastAPI's `BackgroundTasks`. Users can upload a file through the API, and the file is processed in the background while the API immediately returns a success response.

## Features

- Upload files using FastAPI
- Save uploaded files locally
- Process files asynchronously using BackgroundTasks
- Interactive API documentation with Swagger UI

## Technologies Used

- Python
- FastAPI
- Uvicorn

## Project Structure

```
Background-File-Processing/
│
├── uploads/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST /upload

Uploads a file and starts background processing asynchronously.

## Sample Response

```json
{
  "message": "File uploaded successfully. Background processing started.",
  "filename": "sample.pdf"
}
```

## Author

**Shlisha C S**
