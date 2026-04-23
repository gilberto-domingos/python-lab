from fastapi import FastAPI
from src.contexts.campaigns.api.routers.router_registry import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
