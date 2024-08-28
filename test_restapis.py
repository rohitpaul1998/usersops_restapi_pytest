from http.client import responses

import pytest
import requests

baseURL = "https://jsonplaceholder.typicode.com"

# test1: create user
def test_create_new_user():
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Main St",
            "suite": "Apt. 4B",
            "city": "Springfield",
            "zipcode": "12345"
        },
        "phone": "555-555-5555",
        "website": "johndoe.com"
    }

    response = requests.post(f"{baseURL}/users", json=new_user)
    assert response.status_code == 201 #to verify if response status code is 201 Created
    data = response.json()
    assert data["name"] == new_user["name"]
    assert data["username"] == new_user["username"]
    assert data["email"] == new_user["email"]

def test_read_users():
    user_id = 1
    response = requests.get(f"{baseURL}/users/{user_id}")
    assert response.status_code == 200 #to verify if response status code is 200OK
    data = response.json()
    assert data["id"] == user_id
    assert "name" in data #to check if name attribute is present in the response

def test_update_users():
    user_id = 1
    updated_users = {
        "name": "Rohit Paul",
        "username": "rohitpaul10",
        "email": "paul.rohit@dcu.com"
    }
    response = requests.put(f"{baseURL}/users/{user_id}", json=updated_users)
    assert response.status_code == 200 #to verify if the update has been made
    data = response.json()
    assert data["name"] == updated_users["name"]
    assert data["username"] == updated_users["username"]
    assert data["email"] == updated_users["email"]

def test_delete_users():
    user_id = 1
    response = requests.delete(f"{baseURL}/users/{user_id}")
    assert response.status_code == 200



