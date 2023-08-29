"""app module."""
import json

import requests

from users.model import get


def get_user(user_id):
    user = get(user_id)
    print(json.dumps(user))


def sample_req():
    response = requests.get("https://xkcd.com/info.0.json")
    print(response.content)
