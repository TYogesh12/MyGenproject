# SmartSDLC

AI-Enhanced Software Development Lifecycle Assistant

## Setup

1. Copy `.env.example` to `.env`
2. Fill in your actual credentials in `.env`
3. Install dependencies: `pip install -r requirements.txt`
4. Run backend: `uvicorn backend.main:app --reload`
5. Run frontend: `streamlit run frontend/home.py`

## Environment Variables

- `WATSONX_API_KEY`: Your IBM WatsonX API key
- `WATSONX_PROJECT_ID`: Your WatsonX project ID
- `WATSONX_URL`: WatsonX service URL