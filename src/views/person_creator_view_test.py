from .person_creator_view import PersonCreatorView


class MockController:
    def create(self, person_info: dict) -> dict:
        pass


class MockRequest:
    def __init__(self) -> None:
        self.body = {
            "first_name": "Fulano",
            "last_name": "deTal",
            "age": 30,
            "pet_id": 123,
        }


def test_handle():
    controller = MockController()
    http_request = MockRequest()

    person_info = http_request.body
    body_response = controller.create(person_info)
    response = PersonCreatorView(controller).handle(http_request)

    assert response.status_code == 201
    assert response.body == body_response
