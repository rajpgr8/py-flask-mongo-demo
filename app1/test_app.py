import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask API!" in response.data

def test_get_items(client):
    response = client.get('/api/items')
    assert response.status_code == 200
    assert b"items" in response.data

def test_add_item(client):
    response = client.post('/api/items', json={"item": "test item"})
    assert response.status_code == 201
    assert b"Item added successfully" in response.data

    response = client.get('/api/items')
    assert b"test item" in response.data

def test_add_invalid_item(client):
    response = client.post('/api/items', json={})
    assert response.status_code == 400
    assert b"Invalid item" in response.data