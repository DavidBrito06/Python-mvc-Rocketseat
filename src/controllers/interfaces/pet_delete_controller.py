from abc import ABC, abstractmethod


class PetDeleteControllerInterface(ABC):

    @abstractmethod
    def delete_pet(self, name: str) -> None:
        pass
