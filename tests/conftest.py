import pytest
import requests

BASE_URL= "http://127.0.0.1:8000"

@pytest.fixture
def clean_db():
    requests.delete(f"{BASE_URL}/missions")
    yield
    requests.delete(f"{BASE_URL}/missions")

@pytest.fixture
def valid_mission_data():
    return {
        "name": "Apollo 11",
        "agency": "NASA",
        "launch_year": 1969,
        "target": "Moon",
        "status": "COMPLETED",
        "crewed": True,
        "description": "First crewed Moon landing"
    }

@pytest.fixture
def created_mission(clean_db, valid_mission_data):
    response = requests.post(f"{BASE_URL}/missions", json=valid_mission_data)
    return response.json()

@pytest.fixture
def multiple_missions(clean_db):
    missions = [
        {"name": "Apollo 11", "agency": "NASA", "launch_year": 1969, "target": "Moon", "status": "COMPLETED", "crewed": True},
        {"name": "Mars 2020", "agency": "NASA", "launch_year": 2020, "target": "Mars", "status": "ACTIVE", "crewed": False},
        {"name": "Mars Express", "agency": "ESA", "launch_year": 2003, "target": "Mars", "status": "ACTIVE", "crewed": False},
        {"name": "ExoMars", "agency": "ESA", "launch_year": 2028, "target": "Mars", "status": "PLANNED", "crewed": False},
        {"name": "Soyuz MS-25", "agency": "ROSCOSMOS", "launch_year": 2024, "target": "ISS", "status": "COMPLETED", "crewed": True},
    ]
    created = []
    for m in missions:
        response = requests.post(f"{BASE_URL}/missions", json=m)
        created.append(response.json())
    return created