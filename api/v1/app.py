#!/usr/bin/python3
"""Creating the Route needed for the application"""
from api.v1.views import app_views
from flask import Flask
from os import environ
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception=None):
    """Close the storage when the app context is torn down."""
    storage.close()


if __name__ == "__main__":
    HBNB_API_HOST = environ.get('HBNB_API_HOST', '0.0.0.0')
    HBNB_API_PORT = int(environ.get('HBNB_API_PORT', 5000))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
