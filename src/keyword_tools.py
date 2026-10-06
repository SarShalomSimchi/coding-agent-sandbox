def normalize_keyword(value: str) -> str:
    """Normalize one keyword for matching."""
    return " ".join(value.strip().lower().split())


def normalize_keywords(values: list[str]) -> list[str]:
    """Normalize a collection of keywords with stable deduplication."""
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        normalized = normalize_keyword(value)
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return result
