def normalize_keyword(value: str) -> str:
    """Normalize one keyword for matching."""
    return " ".join(value.strip().lower().split())
