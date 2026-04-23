from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_lab.src.contexts.campaigns.api.routers.router_registry import api_router

app = FastAPI()

app.add.middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)