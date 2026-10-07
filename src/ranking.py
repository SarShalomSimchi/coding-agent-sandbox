def top_jobs(jobs: list[dict], limit: int) -> list[dict]:
    """Return up to limit jobs ranked by descending score."""
    if limit <= 0:
        return []
    return sorted(jobs, key=lambda job: job["score"])[:limit]
