def summarize_code(client, prompt: str) -> str:
    """Summarizes the given code using WatsonX Client."""
    return client.generate(f"Summarize this code:\n{prompt}")
