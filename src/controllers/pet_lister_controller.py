from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)

        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    @staticmethod
    def __format_response(pets: list[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
