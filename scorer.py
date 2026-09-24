def judge(_question: str, expects: str, answer: str, _results) -> bool:
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()    