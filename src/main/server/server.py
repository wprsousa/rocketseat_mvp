from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.sqlite.settings.connection import (
    db_connection_handler,
)
from src.main.routes.pets_routes import pets_router

db_connection_handler.connect_to_db()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pets_router)
