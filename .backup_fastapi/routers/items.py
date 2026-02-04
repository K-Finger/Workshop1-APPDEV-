from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# In-memory storage - simple array of strings
items = []


# GET all items
@router.get("/") #Decorators (@app.get, @app.post, etc.) define routes and HTTP methods
def get_items():
    return items # returning from a route function automatically converts it to a JSON response


# GET single item by index
@router.get("/{item_id}")
def get_item(item_id: int): # function params automatically become query params, path params, or request bodies
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# POST create new item
@router.post("/", status_code=201)
def create_item(item: str):
    items.append(item)
    return {"message": "Item created", "item": item}


# PUT update item by index
@router.put("/{item_id}")
def update_item(item_id: int, item: str):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated", "item": item}


# DELETE item by index
@router.delete("/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    removed = items.pop(item_id)
    return {"message": "Item deleted", "item": removed}
