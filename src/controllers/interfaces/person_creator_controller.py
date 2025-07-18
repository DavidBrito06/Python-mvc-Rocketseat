from typing import Dict
from abc import ABC, abstractmethod

class PersonCreatorControllerInterface(ABC):

    @abstractmethod
    def create_person(self, person_info: Dict) -> Dict:
        pass
      