from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import ai_routes, auth_routes, chat_routes, feedback_routes
from dotenv import load_dotenv


load_dotenv()
app = FastAPI(title="SmartSDLC API",
              description="Automated AI-enhanced SDLC Assistant",
              version="1.0.0")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/")
def root(): return {"status": "ok", "message": "Welcome to SmartSDLC API!"}

app.include_router(ai_routes.ai_router, prefix="/ai", tags=["AI"])
app.include_router(auth_routes.auth_router, prefix="/auth", tags=["Auth"])
app.include_router(chat_routes.chat_router, prefix="/chat", tags=["Chat"])
app.include_router(feedback_routes.feedback_router, prefix="/feedback", tags=["Feedback"])
