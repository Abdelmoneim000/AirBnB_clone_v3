#!/bin/bash

HBNB_MYSQL_USER=lorddark0008
HBNB_MYSQL_PWD=lookylooky7
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db
HBNB_TYPE_STORAGE=$2

# Check if an argument (a script) was provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 script_name"
  exit 1
fi

# Check if the script exists and is executable
if [ ! -x "./$1" ]; then
  echo "Error: Script '$1' is not found or not executable."
  exit 1
fi

# Execute the script passed as an argument
./$1
