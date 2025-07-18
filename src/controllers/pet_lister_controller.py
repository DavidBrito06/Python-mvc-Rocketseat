from typing import Dict
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entites.pets import PetsTable

class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    
    def list_pet(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets
    
    def __format_response(self, pets: list[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                "name": pet.name,
                "type": pet.type,
                "id": pet.id
            })
        return {
            "data": {
                "type": "pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }
