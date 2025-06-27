import requests

BACKEND_URL = "http://127.0.0.1:8000"

def post(endpoint: str, payload: dict) -> dict:
    """Send a POST request to the backend."""
    url = f"{BACKEND_URL}{endpoint}"
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

def get(endpoint: str) -> dict:
    """Send a GET request to the backend."""
    url = f"{BACKEND_URL}{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
