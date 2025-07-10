from flask import Flask

from src.auth.route import bp_auth


def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(bp_auth, url_prefix="/v1")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3000, debug=True)
