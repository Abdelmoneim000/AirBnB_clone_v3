#!/bin/bash

unset HBNB_MYSQL_USER
unset HBNB_MYSQL_PWD
unset HBNB_MYSQL_HOST
unset HBNB_MYSQL_DB
unset HBNB_API_HOST
unset HBNB_API_PORT
unset HBNB_TYPE_STORAGE


# Execute the script
python3 -m api.v1.app
