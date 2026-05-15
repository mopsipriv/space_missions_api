import requests

BASE_URL = "http://127.0.0.1:8000"

def test_create_returns_201(clean_db, valid_mission_data):
    response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    assert response.status_code == 201

def test_create_returns_mission_data(clean_db, valid_mission_data):
    response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    data = response.json()
    assert data["name"] == "Apollo 11"
    assert data["agency"] == "NASA"
    assert data["launch_year"] == 1969
    assert data["target"] == "Moon"
    assert data["status"] == "COMPLETED"
    assert data["crewed"] == True
    assert data["description"] == "First crewed Moon landing"

def test_create_assigns_id(clean_db, valid_mission_data):
    response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    data = response.json()
    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["id"] > 0

def test_created_mission_appears_in_database(clean_db, valid_mission_data):
    create_response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    mission_id = create_response.json()["id"]
    
    get_response = requests.get(f"{BASE_URL}/missions/{mission_id}")
    
    assert get_response.status_code == 200
    assert get_response.json()["name"] == valid_mission_data["name"]

def test_id_increments(clean_db, valid_mission_data):
    first_response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    second_response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    
    first_id = first_response.json()["id"]
    second_id = second_response.json()["id"]
    
    assert second_id == first_id + 1

def test_create_without_description(clean_db, valid_mission_data):
    data = valid_mission_data.copy()
    del data["description"]
    
    response = requests.post(f"{BASE_URL}/missions", json=data)
    
    assert response.status_code == 201
    assert response.json()["description"] is None

def test_data_consistency(clean_db, valid_mission_data):
    response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    data = response.json()
    
    for key, value in valid_mission_data.items():
        assert data[key] == value