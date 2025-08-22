from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.auth.route import bp_auth
from src.error_handler.error_handler import bp_erro_handler


def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(bp_auth, url_prefix='/v1')
    return app


if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(bp_erro_handler)

    # Rate Limiter Configuration
    limiter = Limiter(
        get_remote_address, app=app, default_limits=['100 per minute']
    )

    app.run(host='0.0.0.0', port=3000, debug=True)
