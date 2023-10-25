from fastapi.testclient import TestClient
from todo_app.main import app

# under lab6:    pytest --cov=todo_app tests/
client = TestClient(app)

def test_simple_get():
    response = client.get("/simple_get")
    assert response.status_code == 200
    assert response.json() == {"status": "simple GET endpoint"}

def test_get_with_path():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5}

def test_get_with_query():
    response = client.get("/items/", params={"query_param": "example_query"})
    assert response.status_code == 200
    assert response.json() == {"query_param": "example_query"}

def test_get_with_path_and_query():
    response = client.get("/items/5/query/", params={"query_param": "example_query"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "query_param": "example_query"}

def test_post_item():
    test_item = {"key": "value"}
    response = client.post("/post_item/", json=test_item)
    assert response.status_code == 200
    assert response.json() == {"item": test_item}

def test_put_item():
    test_item = {"key": "new_value"}
    response = client.put("/items/5", json=test_item)
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "updated_item": test_item}

def test_delete_item():
    response = client.delete("/items/5")
    assert response.status_code == 200
    assert response.json() == {"status": "item 5 deleted"}
