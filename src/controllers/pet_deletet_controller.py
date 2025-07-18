from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetDeleteController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository
    

    def delete_pet(self, name: str) -> None:
        self.__pets_repository.delete_pet(name)
