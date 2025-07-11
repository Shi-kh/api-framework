from api import users_api

def test_get_user():
    response = users_api.get_user(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_user():
    user = {"name": "Alice", "email": "alice@example.com"}
    response = users_api.create_user(user)
    assert response.status_code == 201

def test_update_user():
    user = {"name": "Bob", "email": "bob@example.com"}
    response = users_api.update_user(1, user)
    assert response.status_code in [200, 201]

def test_delete_user():
    response = users_api.delete_user(1)
    assert response.status_code in [200, 204]
