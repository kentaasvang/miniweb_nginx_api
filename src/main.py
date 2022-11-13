#!./venv/bin/python
from flask import Flask
import nginx


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def create_server_block():
        return {"blocks": ["asvang.no", "kentmartin.net"]}

    return app


if __name__ == "__main__":
    config = {
        "host": "127.0.0.1",
        "port": 8000,
        "debug": True
    }

    app = create_app()
    app.run(**config)