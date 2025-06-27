from fastapi import APIRouter
from pydantic import BaseModel
from backend.services import chat_assistant
from backend.services.watsonx import WatsonXClient
import os

chat_router = APIRouter()
client = WatsonXClient(api_key=os.environ.get("WATSONX_API_KEY"),
                       project_id=os.environ.get("WATSONX_PROJECT_ID"),
                       url=os.environ.get("WATSONX_URL"))

class ChatRequest(BaseModel): prompt: str

@chat_router.post("/chat")
def chat(request: ChatRequest): return {"response": chat_assistant.chat(client, request.prompt)}
