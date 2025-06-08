from src.server_flask.server_flask import app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
