import hashlib

user_db = {"admin": hashlib.sha256(b"admin123").hexdigest()}

def authenticate_user(username: str, password: str) -> bool:
    """Check if the user has valid credentials."""
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return user_db.get(username) == password_hash
