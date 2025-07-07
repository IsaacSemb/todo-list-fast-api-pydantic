from datetime import datetime, timezone


def get_current_utc():
    """
    Return current UTC datetime with timezone info.
    """
    return datetime.now(timezone.utc)