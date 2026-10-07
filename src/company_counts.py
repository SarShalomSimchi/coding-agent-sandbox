def group_job_counts_by_company(jobs: list[dict]) -> dict[str, int]:
    """Count jobs per company, preserving first-seen insertion order."""
    counts: dict[str, int] = {}
    for job in jobs:
        company = job["company"]
        counts[company] = counts.get(company, 0) + 1
    return counts
