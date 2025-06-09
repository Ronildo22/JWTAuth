class HttpResponse:
    """
    Represents an HTTP response.
    This class can be extended to create specific DTOs for different HTTP responses.
    """

    def __init__(
        self,
        payload: dict = None,
        headers: dict = None,
        params: dict = None,
        status_code: int = None,
    ):

        self.payload = payload
        self.headers = headers
        self.params = params
        self.status_code = status_code
