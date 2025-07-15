import pytest
from mock_alchemy.mocking  import UnifiedAlchemyMagicMock
from unittest import mock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entites.people import PeopleTable
from .people_repository import PeopleRepository

class MockConnnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PeopleTable)],
                    [
                        PeopleTable(first_name="David", last_name="Smith", age=30, pet_id=1),
                        PeopleTable(first_name="Maria", last_name="Sousa", age=5, pet_id=2)
                    ]
                )
            ]
        )
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockConnnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_people():
    mock_connection = MockConnnection()
    repo = PeopleRepository(mock_connection)
    response = repo.list_people()

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()


    assert response[0].first_name == "David"

def test_delete_people():
    mock_connection = MockConnnection()
    repo = PeopleRepository(mock_connection)

    repo.delete_people("David")

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.filter.assert_called_once_with(PeopleTable.first_name == "David")
    mock_connection.session.delete.assert_called_once()


def test_list_people_no_result():
    mock_connection = MockConnnectionNoResult()
    repo = PeopleRepository(mock_connection)
    response = repo.list_people()

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_people_no_result():
    mock_connection = MockConnnectionNoResult()
    repo = PeopleRepository(mock_connection)

    with pytest.raises(NoResultFound):
        repo.delete_people("FakeName")
    
    
    