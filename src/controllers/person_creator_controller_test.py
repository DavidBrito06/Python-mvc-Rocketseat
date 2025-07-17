import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, person: dict):
        pass


def test_create_person():
    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123
    }
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create_person(person_info)

    assert response ["data"]["type"] == "person"
    assert response ["data"]["count"] == 1
    assert response ["data"]["attributes"] == person_info

def test_create_person_error():
    person_info = {
        "first_name": "John123",
        "last_name": "Doe000",
        "age": 30,
        "pet_id": 123
    }
    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(ValueError):
        controller.create_person(person_info)