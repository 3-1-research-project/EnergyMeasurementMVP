import requests
from requests import Response
from typing import List, Tuple
import random
import string
from tqdm import tqdm
import argparse

def _generate_random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def seed(register_user_endpoint: str, tweet_endpoint: str, user_amount: int, tweet_per_user_amount: int) -> Tuple[bool, List[Response], List[Response]]:
    register_user_error_responses = []
    tweet_error_responses = []

    for i in tqdm(range(user_amount), desc="Registering Users"):
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

    for i in tqdm(range(user_amount), desc="Posting Tweets"):
        for j in tqdm(range(tweet_per_user_amount), desc=f"User {i} Tweets"):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Seed script for posting tweets.')
    parser.add_argument('register_endpoint', type=str, help='The endpoint for user registration')
    parser.add_argument('tweet_endpoint', type=str, help='The endpoint for posting tweets')
    parser.add_argument('user_amount', type=int, help='The number of users to register')
    parser.add_argument('tweet_per_user_amount', type=int, help='The number of tweets per user')

    args = parser.parse_args()

    (isSuccess, register_user_results, tweet_results) = seed(args.register_endpoint, args.tweet_endpoint, args.user_amount, args.tweet_per_user_amount)

    if (isSuccess):
        print(f"Success, registered {args.user_amount} users and each user tweeted {args.tweet_per_user_amount}")
    else:
        register_user_errors = [result for result in register_user_results if not result.ok]

        if (len(register_user_errors) > 0):
            print(f"Register user returned {len(register_user_errors)} errors, printing the first 5")
            print(register_user_errors[:5])

        tweet_errors = [result for result in tweet_results if not result.ok]
        if (len(tweet_errors) > 0):
            print(f"Tweet for a user returned {len(tweet_errors)} errors, printing the first 5")
            print(tweet_errors[:5])
