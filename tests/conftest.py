import pytest

from main import create_app


@pytest.fixture
def client_http():
    """
    Fixture to create a test client for the Flask application.
    """
    app = create_app()
    with app.test_client() as client:
        yield client
