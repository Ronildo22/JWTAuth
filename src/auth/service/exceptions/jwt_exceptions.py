class JWTInvalidTokenError(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class JWTExpiredSignatureError(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
