from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os

# Import available services
from backend.services.code_generation import generate_code
from backend.services.test_generation import generate_test
from backend.services.bug_fixer import fix_bug
from backend.services.code_summarization import summarize_code
from backend.services.pdf_extraction import extract_text_from_file
from backend.services.chat_assistant import chat
from backend.services.watsonx import WatsonXClient

# Initialize WatsonX Client
client = WatsonXClient(
    api_key=os.environ.get("WATSONX_API_KEY"),
    project_id=os.environ.get("WATSONX_PROJECT_ID"),
    url=os.environ.get("WATSONX_URL")
)

# Create the Router
ai_router = APIRouter()

# Request Model
class PromptRequest(BaseModel): 
    prompt: str

# Route Definitions
@ai_router.post("/generate-code")
def generate(request: PromptRequest): 
    """Generate code from a natural language prompt."""
    return {"response": generate_code(client, request.prompt)}

@ai_router.post("/fix-bug")
def fix(request: PromptRequest): 
    """Fix bugs in a given piece of code."""
    return {"response": fix_bug(client, request.prompt)}

@ai_router.post("/generate-test")
def test(request: PromptRequest): 
    """Generate test cases for the given code."""
    return {"response": generate_test(client, request.prompt)}

@ai_router.post("/summarize-code")
def summarize(request: PromptRequest): 
    return {"response": summarize_code(client, request.prompt)}


@ai_router.post("/chat")
def chat_route(request: PromptRequest): 
    """Chat route that answers questions in a software engineering context."""
    return {"response": chat(client, request.prompt)}

@ai_router.post("/classify-requirement")
def classify(request: PromptRequest):
    """Classify requirements into SDLC phases."""
    prompt = f"Classify this requirement into SDLC phases and explain: {request.prompt}"
    return {"response": client.generate(prompt)}

@ai_router.post("/extract-pdf")
def extract(file: UploadFile = File(...)):
    """Extract text from an uploaded PDF."""
    extracted = extract_text_from_file(file)
    return {"response": extracted}
