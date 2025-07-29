from .person_creator_validator import person_creator_validator

class MockHttpRequest:
    def __init__(self, body):
        self.body = body

def test_person_creator_validator():
    request = MockHttpRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    })

    person_creator_validator(request)