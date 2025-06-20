from flask import Flask

from src.auth.route import bp_auth

app = Flask(__name__)
app.register_blueprint(bp_auth, url_prefix="/v1")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
