from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer
from src.views.http_types.http_request import HttpRequest


person_routes = APIRouter()


@person_routes.post("/people")
async def create_person(request: Request):
    body = await request.json()
    http_request = HttpRequest(body)
    view = person_creator_composer()

    http_response = view.handle(http_request)

    return JSONResponse(
        status_code=http_response.status_code, content=http_response.body
    )


@person_routes.get("/people/{person_id}")
def find_person(person_id: int):
    try:
        http_request = HttpRequest(param={"person_id": person_id})
        view = person_finder_composer()
        http_response = view.handle(http_request)
        return JSONResponse(
            status_code=http_response.status_code, content=http_response.body
        )
    except Exception as error:
        return JSONResponse(status_code=500, content={"error": str(error)})
