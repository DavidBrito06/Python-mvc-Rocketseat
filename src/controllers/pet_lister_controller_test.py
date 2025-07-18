from src.models.sqlite.entites.pets import PetsTable
from .pet_lister_controller import PetListerController

# Mock separado
class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=1, name="Fido", type="dog"),
            PetsTable(id=2, name="Whiskers", type="cat"),
            PetsTable(id=3, name="Polly", type="bird"),
        ]

# Função de teste fora da classe
def test_list_pet():
    controller = PetListerController(MockPetsRepository())
    response = controller.list_pet()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 3,
            "attributes": [
                {"name": "Fido", "type": "dog", "id": 1},
                {"name": "Whiskers", "type": "cat", "id": 2},
                {"name": "Polly", "type": "bird", "id": 3}
            ]
        }
    }

    assert response == expected_response
