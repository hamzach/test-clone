"""Get user module."""

from users.db import USERS


def get(user_id) -> dict:
    return USERS.get(user_id)
