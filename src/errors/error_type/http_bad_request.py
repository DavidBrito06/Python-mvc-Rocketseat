class HttpBadRequestError(Exception):
    def __init__(self, message: str):
        self.status_code = 400
        self.name = "Bad Request"
        self.message = message
        super().__init__(self.message)
       