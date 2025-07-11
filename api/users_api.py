import requests
from utils import config

def get_user(user_id):
    return requests.get(f"{config.BASE_URL}/users/{user_id}")

def create_user(user_data):
    return requests.post(f"{config.BASE_URL}/users", json=user_data)

def update_user(user_id, user_data):
    return requests.put(f"{config.BASE_URL}/users/{user_id}", json=user_data)

def delete_user(user_id):
    return requests.delete(f"{config.BASE_URL}/users/{user_id}")
