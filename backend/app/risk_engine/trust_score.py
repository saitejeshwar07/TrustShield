def calculate_trust_score(risk: int):

    score = 100 - risk

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score