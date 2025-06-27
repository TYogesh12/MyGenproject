from fastapi import APIRouter
from pydantic import BaseModel

feedback_router = APIRouter()

class Feedback(BaseModel): message: str

@feedback_router.post("/submit")
def submit_feedback(data: Feedback): 
    """Accept feedback (no storage)."""
    return {"status": "ok", "message": "Thank you for your feedback!"}
