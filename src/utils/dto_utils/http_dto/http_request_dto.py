class HttpRequestDTO:
    """
    Base class for HTTP Data Transfer Objects (DTOs).
    This class can be extended to create specific DTOs for different HTTP requests and responses.
    """

    def __init__(
        self, payload: dict = None, headers: dict = None, params: dict = None
    ):
        """
        Initializes the HttpRequest with optional payload, headers, and parameters.

        :param payload: The data to be sent in the request body.
        :param headers: The headers to be included in the request.
        :param params: The query parameters to be included in the request URL.
        """

        self.payload = payload
        self.headers = headers
        self.params = params
