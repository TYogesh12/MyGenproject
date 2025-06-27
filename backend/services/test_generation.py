def generate_test(client, code: str) -> str:
    """Generates test cases for the given code."""
    return client.generate(f"Write test cases for: {code}")
