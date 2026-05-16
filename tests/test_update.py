import requests

BASE_URL = "http://127.0.0.1:8000"

def test_put_replaces_mission(created_mission, valid_mission_data):
    mission_id=created_mission["id"]
    new_data = valid_mission_data.copy()
    new_data["name"] = "Artemis II"

    response = requests.put(f"{BASE_URL}/missions/{mission_id}", json=new_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Artemis II"

def test_put_nonexistent_returns_404(clean_db, valid_mission_data):
    invalid_id= 999
    response = requests.put(f"{BASE_URL}/missions/{invalid_id}", json=valid_mission_data)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Mission is not found"

def test_patch_updates_single_field(created_mission):
    mission_id=created_mission["id"]
    response = requests.patch(f"{BASE_URL}/missions/{mission_id}", json={"status": "FAILED"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "SUCCESS"
    assert data["name"] == created_mission["name"]
    assert data["agency"] == created_mission["agency"]
    assert data["launch_year"] == created_mission["launch_year"]

def test_patch_updates_multiple_fields(created_mission):
    mission_id=created_mission["id"]
    response = requests.patch(f"{BASE_URL}/missions/{mission_id}", json={"status": "COMPLETED","name": "NASA"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "COMPLETED"
    assert data["name"] == "NASA"
    assert data["agency"] == created_mission["agency"]
    assert data["launch_year"] == created_mission["launch_year"]

def test_patch_nonexistent_returns_404(clean_db, valid_mission_data):
    invalid_id=999
    response = requests.patch(f"{BASE_URL}/missions/{invalid_id}", json=valid_mission_data)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Mission is not found"