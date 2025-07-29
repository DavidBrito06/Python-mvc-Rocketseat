class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        self.status_code = 422
        self.name = "Unprocessable Entity"
        self.message = message
        super().__init__(self.message)
       