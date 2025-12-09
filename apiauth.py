import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_with_retries(endpoint, params=None, max_attempts=3, delay_seconds=2):
    url = BASE_URL + endpoint
    for attempt in range(max_attempts):
        try:
            print(f"Requesting {url} (attempt {attempt + 1})")
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            if attempt < max_attempts - 1:
                print(f"Retrying in {delay_seconds} seconds...")
                time.sleep(delay_seconds)
            else:
                print("Max attempts reached. Giving up.")
                raise

def fetch_user(user_id):
    response = get_with_retries(f"/users/{user_id}")
    return response.json()

def fetch_posts_for_user(user_id):
    response = get_with_retries("/posts", params={"userId": user_id})
    return response.json()

def main():
    user_id = 1

    print("Fetching user information...")
    user = fetch_user(user_id)
    print("User name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("-" * 40)

    print("Fetching posts for this user...")
    posts = fetch_posts_for_user(user_id)
    print(f"Found {len(posts)} posts.")
    print("-" * 40)

    for post in posts:
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:")
        print(post["body"])
        print("-" * 40)

if __name__ == "__main__":
    main()
