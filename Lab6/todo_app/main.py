from fastapi import FastAPI

app = FastAPI()


# under lab6 path:  uvicorn todo_app.main:app --reload
#in Chrome:  curl 'http://localhost:8000/simple_get'




# Create a GET ReST API
@app.get("/simple_get")
def simple_get():
    return {"status": "simple GET endpoint"}

# Create a GET ReST API with path parameters
@app.get("/items/{item_id}")
def get_with_path(item_id: int):
    return {"item_id": item_id}

# Create a GET ReST API with query parameters
@app.get("/items/")
def get_with_query(query_param: str):
    return {"query_param": query_param}

# Create a GET ReST API with path parameters AND query parameters
@app.get("/items/{item_id}/query/")
def get_with_path_and_query(item_id: int, query_param: str):
    return {"item_id": item_id, "query_param": query_param}

# Create a POST ReST API
@app.post("/post_item/")
def post_item(item: dict):
    return {"item": item}

# Create a PUT ReST API
@app.put("/items/{item_id}")
def put_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

# Create a DELETE ReST API
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"status": f"item {item_id} deleted"}
