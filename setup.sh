#!/bin/bash

VENV_DIR=".venv"

python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

python3 -m pip install -r $HOME/django-piscine/requirements.txt
