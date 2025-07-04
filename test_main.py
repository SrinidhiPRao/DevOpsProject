import pytest
from fastapi.testclient import TestClient
from uuid import UUID

from main import app  

client = TestClient(app)

def test_create_note():
    response = client.post("/notes", json={
        "title": "Test Note",
        "content": "This is a test note."
    })
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert UUID(data["id"])  # Check if valid UUID
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note."

def test_get_all_notes():
    response = client.get("/notes")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # At least the one from previous test

def test_read_note():
    # First, create a note
    post_resp = client.post("/notes", json={
        "title": "Read Me",
        "content": "Check me out!"
    })
    note_id = post_resp.json()["id"]

    # Now, get the note
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == note_id
    assert data["title"] == "Read Me"

def test_update_note():
    # Create a note
    post_resp = client.post("/notes", json={
        "title": "Update Me",
        "content": "Before update"
    })
    note_id = post_resp.json()["id"]

    # Update it
    response = client.put(f"/notes/{note_id}", json={
        "title": "Updated Title",
        "content": "After update"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["content"] == "After update"

def test_delete_note():
    # Create a note
    post_resp = client.post("/notes", json={
        "title": "Delete Me",
        "content": "You won't see me again."
    })
    note_id = post_resp.json()["id"]

    # Delete it
    del_resp = client.delete(f"/notes/{note_id}")
    assert del_resp.status_code == 200
    assert del_resp.json()["message"] == "Note deleted"

    # Confirm it's gone
    get_resp = client.get(f"/notes/{note_id}")
    assert get_resp.status_code == 404

def test_note_not_found():
    fake_id = "12345678-1234-5678-1234-567812345678"

    get_resp = client.get(f"/notes/{fake_id}")
    assert get_resp.status_code == 404

    put_resp = client.put(f"/notes/{fake_id}", json={"title": "x", "content": "y"})
    assert put_resp.status_code == 404

    del_resp = client.delete(f"/notes/{fake_id}")
    assert del_resp.status_code == 404
