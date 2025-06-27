def fix_bug(client, bug_code: str) -> str:
    """Fixes bugs in the given code."""
    return client.generate(f"Fix this bug: {bug_code}")
