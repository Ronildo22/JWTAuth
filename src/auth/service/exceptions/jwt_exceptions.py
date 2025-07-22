class JWTInvalidTokenError(Exception):

    def __init__(self):
        self.message = "Invalid token"
        super().__init__(self.message)


class JWTExpiredSignatureError(Exception):

    def __init__(self):
        self.message = "Token has expired"
        super().__init__(self.message)
