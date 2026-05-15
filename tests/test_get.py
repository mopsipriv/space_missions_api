import requests

BASE_URL = "http://127.0.0.1:8000"

def test_empty_db_returns_empty_list(clean_db):
    response = requests.get(f"{BASE_URL}/missions")
    assert response.status_code == 200
    data = response.json()
    assert data == []
    
def test_get_all_missions(clean_db):
    mission1={"name": "Vostok 1", "agency": "ROSCOSMOS", "launch_year": 1961,
        "target": "Earth Orbit", "status": "COMPLETED", "crewed": True, "description": "First flight "
    }

    mission2 = {
        "name": "Apollo 11", "agency": "NASA", "launch_year": 1969,
        "target": "Moon", "status": "COMPLETED", "crewed": True, "description": "First crewed Moon landing"
    }

    mission3 = {
        "name": "Mars 2020", "agency": "NASA", "launch_year": 2020,
        "target": "Mars", "status": "COMPLETED", "crewed": False, "description": "Perseverance"
    }
    for mission in [mission1, mission2, mission3]:
        requests.post(f"{BASE_URL}/missions", json=mission)
    response = requests.get(f"{BASE_URL}/missions")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_missions_by_id(created_mission):
    mission_id=created_mission["id"]
    response = requests.get(f"{BASE_URL}/missions/{mission_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == mission_id

def test_get_nonexistent_mission_returns_404(clean_db):
    invalid_id= 999
    response = requests.get(f"{BASE_URL}/missions/{invalid_id}")
    assert response.status_code == 404
    data=response.json()
    assert data["detail"] == "Mission is not found"

