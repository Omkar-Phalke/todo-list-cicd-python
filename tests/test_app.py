import pytest
from app import app, tasks

@pytest.fixture()
def client():
    tasks.clear()
    with app.test_client() as test_client:
        yield test_client
    tasks.clear()

def test_home_returns_api_information(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "To-Do List API is running"

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_create_and_list_task(client):
    response = client.post("/tasks", json={"title": "Finish assignment"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Finish assignment"
    assert response.get_json()["completed"] is False
    listed = client.get("/tasks")
    assert listed.status_code == 200
    assert len(listed.get_json()) == 1

def test_reject_empty_task_title(client):
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400
    assert "error" in response.get_json()
