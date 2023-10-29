#!/bin/bash

HBNB_MYSQL_USER=lorddark0008
HBNB_MYSQL_PWD=lookylooky7
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db
HBNB_API_HOST="0.0.0.0"
HBNB_API_PORT=5000
HBNB_TYPE_STORAGE=db


# Execute the script
python3 -m api.v1.app
