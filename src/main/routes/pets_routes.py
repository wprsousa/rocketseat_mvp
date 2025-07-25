from fastapi import APIRouter
from fastapi.responses import JSONResponse


pets_router = APIRouter()


@pets_router.get("/pets")
def list_pets():
    return JSONResponse(status_code=200, content={"Olá": "mundo"})
