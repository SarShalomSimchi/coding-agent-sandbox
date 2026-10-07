def normalize_company_name(name: str) -> str:
    """Normalize a company name for matching."""
    return " ".join(name.strip().lower().split())
