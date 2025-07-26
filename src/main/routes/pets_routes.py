from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer


pets_router = APIRouter()


@pets_router.get("/pets")
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_lister_composer()
        http_response = view.handle(http_request)

        return JSONResponse(
            status_code=http_response.status_code, content=http_response.body
        )
    except Exception as error:
        return JSONResponse(status_code=500, content={"error": str(error)})


@pets_router.delete("/pets/{pet_name}")
def delete_pet(pet_name: str):
    try:
        http_request = HttpRequest(param={"name": pet_name})
        view = pet_deleter_composer()
        http_response = view.handle(http_request)

        return JSONResponse(
            status_code=http_response.status_code, content=http_response.body
        )
    except Exception as error:
        return JSONResponse(status_code=500, content={"error": str(error)})
