def filter_jobs_by_min_score(jobs: list[dict], min_score: float) -> list[dict]:
    """Return a new list of jobs whose score is at least min_score, in input order."""
    return [job for job in jobs if job["score"] >= min_score]
