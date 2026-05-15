import requests

BASE_URL = "http://127.0.0.1:8000"

def test_delete_returns_204(created_mission):
    mission_id=created_mission["id"]
    response = requests.delete(f"{BASE_URL}/missions/{mission_id}")
    assert response.status_code == 204
    get_response = requests.get(f"{BASE_URL}/missions/{mission_id}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Mission is not found"

def delete_nonexistent_returns_404(clean_db):
    invalid_id=999
    response = requests.delete(f"{BASE_URL}/missions/{invalid_id}")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Mission is not found"

def test_delete_all(created_mission):
    response = requests.delete(f"{BASE_URL}/missions")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "All missions are deleted"
    get_response = requests.get(f"{BASE_URL}/missions")
    assert get_response.json() == []