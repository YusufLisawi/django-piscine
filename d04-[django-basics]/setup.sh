#!/bin/bash

VENV_DIR=".venv"
PROJECT_NAME="d04"

python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

python3 -m pip install -r requirements.txt

django-admin startproject $PROJECT_NAME