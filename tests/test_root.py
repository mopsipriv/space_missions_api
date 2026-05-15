import requests
BASE_URL = "http://127.0.0.1:8000"

def test_root_returns_200():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

def test_root_returns_message():
    response = requests.get(f"{BASE_URL}/")
    data = response.json()
    assert "message" in data