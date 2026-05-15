import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.parametrize("invalid_agency", ["BLABLA", "nasa", "", "123"])
def test_invalid_agency_rejected(invalid_agency, clean_db, valid_mission_data):
    data = valid_mission_data.copy()
    data["agency"] = invalid_agency
    response = requests.post(f"{BASE_URL}/missions", json=data)
    assert response.status_code == 422

@pytest.mark.parametrize("invalid_status", ["UNKNOWN", "active", "", "DONE"])
def test_invalid_status_rejected(invalid_status, clean_db, valid_mission_data):
    data = valid_mission_data.copy()
    data["status"] = invalid_status
    response = requests.post(f"{BASE_URL}/missions", json=data)
    assert response.status_code == 422

@pytest.mark.parametrize("invalid_launch_year", [1900, 1956, 2100, 5000, -1])
def test_invalid_launch_year_rejected(invalid_launch_year, clean_db, valid_mission_data):
    data = valid_mission_data.copy()
    data["launch_year"] = invalid_launch_year
    response = requests.post(f"{BASE_URL}/missions", json=data)
    assert response.status_code == 422

@pytest.mark.parametrize("field_to_remove", ["name", "agency", "launch_year", "target", "status", "crewed"])
def test_missing_required_field(field_to_remove, clean_db, valid_mission_data):
    data = valid_mission_data.copy()
    del data[field_to_remove]
    response = requests.post(f"{BASE_URL}/missions", json=data)
    assert response.status_code == 422

@pytest.mark.parametrize("invalid_name", ["", "A" * 101])
def test_invalid_name_length(invalid_name, clean_db, valid_mission_data):
    data = valid_mission_data.copy()
    data["name"] = invalid_name
    response = requests.post(f"{BASE_URL}/missions", json=data)
    assert response.status_code == 422