from fastapi import APIRouter
from backend.auth.security import authenticate_user
from backend.auth.user import User

auth_router = APIRouter()

@auth_router.post("/login")
def login(user: User):
    """Login Route (Placeholder)."""
    if authenticate_user(user.username, user.password):
        return {"status": "ok", "user": user.username}
    return {"status": "error", "error": "Invalid credentials"}
