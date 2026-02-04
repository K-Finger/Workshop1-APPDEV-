from fastapi import FastAPI
from routers.root import router as root_router
from routers.items import router as items_router

app = FastAPI()

# Include routers - each router handles a group of related endpoints
app.include_router(root_router)
app.include_router(items_router)
