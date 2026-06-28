from app.risk_engine.risk_rules import *
from app.risk_engine.trust_score import calculate_trust_score


def evaluate_login(
    new_device=False,
    new_country=False,
    new_browser=False,
    new_ip=False,
    unusual_login_time=False,
    failed_attempts=0,
    trusted_device=False,
):

    risk = 0

    if new_device:
        risk += NEW_DEVICE

    if new_country:
        risk += NEW_COUNTRY

    if new_browser:
        risk += NEW_BROWSER

    if new_ip:
        risk += NEW_IP

    if unusual_login_time:
        risk += UNUSUAL_LOGIN_TIME

    if failed_attempts >= 3:
        risk += TOO_MANY_FAILED_ATTEMPTS

    if trusted_device:
        risk += TRUSTED_DEVICE

    trust_score = calculate_trust_score(risk)

    if trust_score >= 80:
        decision = "ALLOW"

    elif trust_score >= 50:
        decision = "STEP_UP_AUTH"

    else:
        decision = "BLOCK"

    return {
        "risk": risk,
        "trust_score": trust_score,
        "decision": decision,
    }