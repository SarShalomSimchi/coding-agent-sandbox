def deduplicate_jobs(jobs: list[dict]) -> list[dict]:
    """Deduplicate jobs by normalized company/title key, keeping first occurrence."""
    seen: set[tuple[str, str]] = set()
    result: list[dict] = []
    for job in jobs:
        key = (
            str(job["company"]).strip().lower(),
            str(job["title"]).strip().lower(),
        )
        if key not in seen:
            seen.add(key)
            result.append(job)
    return result
