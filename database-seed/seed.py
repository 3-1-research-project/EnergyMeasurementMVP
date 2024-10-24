import requests
from requests import Response
from typing import List, Tuple
import random
import string

def seed(register_user_endpoint: str, tweet_endpoint: str, user_amount: int, tweet_per_user_amount: int) -> Tuple[bool, List[Response], List[Response]]:
    register_user_error_responses = []
    tweet_error_responses = []

    for i in range (user_amount):
        username = f"seed_user_{i}"
        email = f"seed_user_{i}@mail.com"
        password = f"seed_{i}"

        response = requests.post(
            url=register_user_endpoint,
            json={
                'username': username,
                'email': email,
                'pwd': password,
            }
        )

        if not response.ok:
            register_user_error_responses.append(response)

    if len(register_user_error_responses) > 0:
        return (False, register_user_error_responses, tweet_error_responses)

    for i in range (user_amount):
        for j in range (tweet_per_user_amount):
            tweet_length = j + 1 if j + 1 < 280 else 280

            response = requests.post(
                url=f"{tweet_endpoint}/seed_user_{i}",
                json={
                    'content': _generate_random_string(tweet_length),
                }
            )

            if not response.ok:
                tweet_error_responses.append(response)
    
    if len(tweet_error_responses) > 0:
        return (False, register_user_error_responses, tweet_error_responses)

    return (True, register_user_error_responses, tweet_error_responses)

def _generate_random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
