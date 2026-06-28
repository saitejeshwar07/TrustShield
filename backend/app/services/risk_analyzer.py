from app.services.browser_service import browser_changed
from app.services.device_service import is_trusted_device
from app.services.ip_service import ip_changed

def analyze_login(device, db):
    trusted = is_trusted_device(
        user_id=device.user_id,
        device_id=device.device_id,
        db=db,
    )

    browser = browser_changed(
        user_id=device.user_id,
        current_browser=device.browser,
        db=db,
    )
    ip = ip_changed(
        user_id=device.user_id,
        current_ip=device.ip_address,
        db=db,
    )

    return {
        "new_device": not trusted,
        "trusted_device": trusted,
        "new_browser": browser,
        "new_ip": False,
        "new_country": False,
        "unusual_login_time": False,
        "failed_attempts": 0,
    }