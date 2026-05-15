import requests

BASE_URL = "http://127.0.0.1:8000"

def test_stats_empty_db(clean_db):
    response = requests.get(f"{BASE_URL}/stats")
    assert response.status_code == 200
    data = response.json()
    
    assert data["total"] == 0
    assert data["by_agency"] == {}
    assert data["by_status"] == {}
    assert data["crewed_count"] == 0

def test_stats_with_missions(multiple_missions):
    response = requests.get(f"{BASE_URL}/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 5
    assert data["by_agency"]["NASA"] == 2
    assert data["by_agency"]["ESA"] == 2
    assert data["by_agency"]["ROSCOSMOS"] == 1
    assert data["by_status"]["COMPLETED"] == 2
    assert data["by_status"]["ACTIVE"] == 2
    assert data["by_status"]["PLANNED"] == 1

def test_stats_crewed_count(multiple_missions):
    response = requests.get(f"{BASE_URL}/stats")
    data = response.json()
    assert data["crewed_count"] == 2