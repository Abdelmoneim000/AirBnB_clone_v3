#!/usr/bin/python3
"""
A module to handle the status messages
"""
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """define the status message"""
    response = {
        "status": "OK"
        }
    return response
