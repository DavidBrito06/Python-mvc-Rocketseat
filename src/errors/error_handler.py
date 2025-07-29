from src.views.http_types.http_response import HttpResponse
from .error_type.http_bad_request import HttpBadRequestError
from .error_type.http_not_found import HttpNotFoundError
from .error_type.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code= error.status_code,
            body={"error":  [{
                "title": error.name,
                "detail": error.message,
            }]}
        )
    return HttpResponse(
        status_code=500,
        body={"error":  [{
            "title": "Internal Server Error",
            "detail": "An unexpected error occurred."
        }]}
    )