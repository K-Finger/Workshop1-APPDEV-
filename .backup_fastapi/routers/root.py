from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/")
def read_root():
    return {"message": "You successfully did a GET!"}


@router.post("/")
def create_item():
    return {"message": "You successfully did a POST!"}


# What about PUT and DELETE routes?
