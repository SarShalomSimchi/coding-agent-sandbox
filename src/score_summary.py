def score_summary(jobs: list[dict]) -> dict:
    """Summarize job scores without mutating the input.

    Returns count, min_score, max_score and average_score. For an empty
    list every numeric field is None and count is 0.
    """
    scores = [job["score"] for job in jobs]
    if not scores:
        return {
            "count": 0,
            "min_score": None,
            "max_score": None,
            "average_score": None,
        }
    return {
        "count": len(scores),
        "min_score": min(scores),
        "max_score": max(scores),
        "average_score": sum(scores) / len(scores),
    }
