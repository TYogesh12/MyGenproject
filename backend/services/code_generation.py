def generate_code(client, prompt: str) -> str:
    """Generates production-ready code from a prompt."""
    return client.generate(f"Write production-ready code for: {prompt}")