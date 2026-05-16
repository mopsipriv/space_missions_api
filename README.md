# Space Missions API

A small REST API for managing space missions, built with FastAPI and tested with pytest + requests.

This project was made as part of the **Testing Tools Workshop** (Testaustyökalujen työpaja) at Oulu University of Applied Sciences (OAMK).

## What it does

The API manages a database of space missions. Each mission has a name, agency, launch year, target, status, and a flag for whether it was crewed.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/missions` | List all missions (supports filters) |
| GET | `/missions/{id}` | Get a single mission |
| POST | `/missions` | Create a new mission |
| PUT | `/missions/{id}` | Replace a mission |
| PATCH | `/missions/{id}` | Update part of a mission |
| DELETE | `/missions/{id}` | Delete a mission |
| DELETE | `/missions` | Delete all missions |
| GET | `/stats` | Get statistics |

Filters for `GET /missions`: `agency`, `status`, `crewed`, `year_from`, `year_to`.

## Tech stack

- **FastAPI** — web framework
- **Pydantic** — data validation
- **Uvicorn** — ASGI server
- **pytest** — testing framework
- **requests** — HTTP client for tests
- **pytest-html** — HTML test reports

## Getting started

### Requirements
- Python 3.9 or newer

### Setup

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux

```

### Run the API

```bash
uvicorn api.main:app --reload
```

The API will be available at http://127.0.0.1:8000.
Interactive Swagger docs: http://127.0.0.1:8000/docs

### Run the tests

The API must be running in another terminal before running the tests.

```bash
pytest -v
```

To generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Project structure

```
testaus-tyopaja/
├── api/
│   ├──__init__.py
│   ├── database.py
│   ├── main.py          # FastAPI app and endpoints
│   └── models.py        # Pydantic models
├── tests/
│   ├── conftest.py      # pytest fixtures
│   ├── test_root.py
│   ├── test_post.py
│   ├── test_get.py
│   ├── test_update.py
│   ├── test_delete.py
│   ├── test_filters.py
│   ├── test_validation.py
│   └── test_stats.py
├── pytest.ini
└── README.md
```

## Tests

The project contains 48 test cases across 9 test files, covering:

- Positive cases (CRUD operations)
- Negative cases (404, 422 responses)
- Parameterized validation tests
- Filter logic
- Statistics calculation

## License

MIT
