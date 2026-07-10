# FastAPI Health & Echo Service

## Project Description

This project is a simple FastAPI application developed to demonstrate REST API development using Python. It includes two endpoints, logging functionality, and exception handling.

## Features

- GET `/health` endpoint to check the application status.
- POST `/echo` endpoint to return the message sent by the user.
- Logging using Python's `logging` module.
- Exception handling using `HTTPException`.
- Automatic API documentation using Swagger UI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```
FastAPI_Project/
│
├── main.py
├── requirements.txt
├── README.md
└── logs/
    └── app.log
```

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd FastAPI_Project
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using Uvicorn.

```bash
uvicorn main:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## Endpoints

### 1. GET /health

Returns the health status of the application.

**Response**

```json
{
    "status": "healthy"
}
```

---

### 2. POST /echo

Accepts a message from the user and returns the same message.

**Request**

```json
{
    "message": "Hello FastAPI"
}
```

**Response**

```json
{
    "echo": "Hello FastAPI"
}
```

---

### Exception Handling

If an empty message is sent:

**Request**

```json
{
    "message": ""
}
```

**Response**

```json
{
    "detail": "Message cannot be empty"
}
```

Status Code:

```
400 Bad Request
```

## Logging

The application records all requests and events in:

```
logs/app.log
```

Example log:

```
2026-07-10 12:38:18 - INFO - Received message: Hello FastAPI
2026-07-10 12:38:18 - INFO - Message echoed successfully
2026-07-10 12:46:48 - WARNING - Empty message received
```

## Author

**Shlisha C S**

## License

This project was developed as part of an AI & Cloud Internship for learning purposes.
