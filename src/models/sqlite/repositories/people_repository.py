from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entites.people import PeopleTable
from src.models.sqlite.entites.pets import PetsTable

class PeopleRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_people(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                person_data = PeopleTable(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_id=pet_id
                )
                database.session.add(person_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_person(self, person_id: int) -> PeopleTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(PeopleTable)
                    .outerjoin(PetsTable, PeopleTable.pet_id == PetsTable.id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label('pet_name'),
                        PetsTable.type.label('pet_type')
                    )
                    .one()
                )
                return person

            except NoResultFound:
                return None
           
    

    def list_people(self) -> List:
        with self.__db_connection as database:
            try:
                people = database.session.query(PeopleTable).all()
                return people
            except NoResultFound:
                return []
    
    def delete_people(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(PeopleTable).filter(PeopleTable.first_name == name).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
