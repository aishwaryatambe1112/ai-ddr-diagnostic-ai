def score_issue(text):

    score = 0

    if "crack" in text.lower():
        score += 3

    if "dampness" in text.lower():
        score += 2

    if "leakage" in text.lower():
        score += 3

    if "vegetation growth" in text.lower():
        score += 2

    if "hollow" in text.lower():
        score += 2

    if score >= 6:
        return "HIGH"

    if score >= 3:
        return "MEDIUM"

    return "LOW"
