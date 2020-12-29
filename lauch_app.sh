#!/bin/bash

pip install -r requirements.txt

myvenv/Scripts/activate.bat

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run
