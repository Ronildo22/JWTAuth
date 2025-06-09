from flask import Flask

app = Flask(__name__)


if __name__ == "__main__":
    app.run(hostclear="0.0.0.0", port=3000, debug=True)
