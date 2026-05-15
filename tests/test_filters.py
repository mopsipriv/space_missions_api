import requests

BASE_URL = "http://127.0.0.1:8000"

def test_filter_by_agency(multiple_missions):
    response = requests.get(f"{BASE_URL}/missions", params={"agency": "NASA"})
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 2
    for mission in data:
        assert mission["agency"] == "NASA"

def test_filter_by_status(multiple_missions):
    response = requests.get(f"{BASE_URL}/missions", params={"status": "ACTIVE"})
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 2
    for mission in data:
        assert mission["status"] == "ACTIVE"

def test_filter_by_crewed(multiple_missions):
    response = requests.get(f"{BASE_URL}/missions", params={"crewed": True})
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 2
    for mission in data:
        assert mission["crewed"] is True

def test_filter_by_year_range(multiple_missions):
    response = requests.get(f"{BASE_URL}/missions", params={"year_from": 2000, "year_to": 2024})
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 3