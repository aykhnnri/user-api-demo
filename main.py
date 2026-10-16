import os
import requests

from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL")

new_post = {
    "title": "Learning APIs",
    "body": "My first POST request",
    "userId": 1
}

response = requests.post(
    base_url + "/posts",
    json=new_post
)

print(response.status_code)
print(response.json())