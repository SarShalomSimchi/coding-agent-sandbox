def deduplicate_jobs(jobs: list[dict]) -> list[dict]:
    """Deduplicate jobs by normalized company/title key, keeping highest scoring job per group."""
    groups: dict[tuple[str, str], dict] = {}
    for job in jobs:
        key = (
            str(job["company"]).strip().lower(),
            str(job["title"]).strip().lower(),
        )
        if key not in groups:
            groups[key] = job
        elif job["score"] > groups[key]["score"]:
            groups[key] = job
    return list(groups.values())
