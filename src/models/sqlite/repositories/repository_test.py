import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository


#db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="This test requires a valid pet_id")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

@pytest.mark.skip(reason="This test requires a valid pet_id")
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name)

@pytest.mark.skip(reason="This test requires a valid pet_id")
def test_insert_person():
   first_name = "David"
   last_name = "Smith"
   age = 30
   pet_id = 1
   repo = PeopleRepository(db_connection_handler)
   repo.insert_people(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="This test requires a valid pet_id")
def test_get_person():
   person_id = 1
   repo = PeopleRepository(db_connection_handler)
   response = repo.get_person(person_id)
   print()
   print(response)
