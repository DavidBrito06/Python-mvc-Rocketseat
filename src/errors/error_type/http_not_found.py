class HttpNotFoundError(Exception):
    def __init__(self, message: str):
        self.status_code = 404
        self.name = "Not Found"
        self.message = message
        super().__init__(self.message)
       