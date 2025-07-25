from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.composer.person_creator_composer import person_creator_composer
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
