def chat(client, prompt: str) -> str:
    """Handles chat queries."""
    return client.generate(f"Answer this in the context of software engineering: {prompt}")
