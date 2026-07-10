from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging
import os

# -----------------------------------
# Create logs folder if it doesn't exist
# -----------------------------------
if not os.path.exists("logs"):
    os.makedirs("logs")

# -----------------------------------
# Logging Configuration
# -----------------------------------
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# -----------------------------------
# Create FastAPI App
# -----------------------------------
app = FastAPI(
    title="FastAPI Health & Echo Service",
    description="Simple FastAPI service with logging and exception handling",
    version="1.0"
)

# -----------------------------------
# Request Model
# -----------------------------------
class Message(BaseModel):
    message: str

# -----------------------------------
# GET /health Endpoint
# -----------------------------------
@app.get("/health")
def health():
    logger.info("Health endpoint accessed")

    return {
        "status": "healthy"
    }

# -----------------------------------
# POST /echo Endpoint
# -----------------------------------
@app.post("/echo")
def echo(data: Message):
    try:
        logger.info(f"Received message: {data.message}")

        # Check if message is empty
        if data.message.strip() == "":
            logger.warning("Empty message received")
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty"
            )

        logger.info("Message echoed successfully")

        return {
            "echo": data.message
        }

    except HTTPException:
        raise

    except Exception:
        logger.exception("Unexpected error occurred")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

# -----------------------------------
# Global Exception Handler
# -----------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.exception(f"Unhandled Exception: {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "Something went wrong"
        }
    )