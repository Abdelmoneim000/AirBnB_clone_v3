#!/usr/bin/python3
"""Creating the Route needed for the application"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown the storage"""
    storage.close()

if __name__ == "__main__":
    HBNB_API_HOST = environ.get('HBNB_API_HOST')
    HBNB_API_PORT = environ.get('HBNB_API_PORT')
    app.run(host=HBNB_API_HOST or '0.0.0.0', port=HBNB_API_PORT or 5000, threaded=True)