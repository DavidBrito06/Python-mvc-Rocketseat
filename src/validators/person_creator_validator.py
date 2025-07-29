from pydantic import BaseModel, constr
from src.views.http_types.http_request import HttpRequest
from src.errors.error_type.http_unprocessable_entity import HttpUnprocessableEntityError

def person_creator_validator(http_request: HttpRequest):
    class PersonCreator(BaseModel):
        first_name: constr(min_length= 1) # type: ignore
        last_name: constr(min_length= 1) # type: ignore
        age: int
        pet_id: int

    try:
        PersonCreator(**http_request.body)
    except Exception as e:
        raise HttpUnprocessableEntityError(f"Invalid person creator data: {e}") from e
