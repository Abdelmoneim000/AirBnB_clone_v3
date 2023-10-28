#!/usr/bin/python3
"""
A module to handle the status messages
"""
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """define the status message"""
    response = {
        "status": "OK"
        }
    return response


@app_views.route('/stats', methods=['GET'])
def get_number_of_objects():
    """A route to count the number of every object type"""
    obj = {
        "amenity": storage.count("amenity"),
        "base_model": storage.count("baseModel"),
        "city": storage.count("city"),
        "place": storage.count("place"),
        "review": storage.count("review"),
    }
    return obj
