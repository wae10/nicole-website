# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.routes import routes


load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)