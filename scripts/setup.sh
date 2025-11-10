#!/bin/bash

python3 -m venv work
source work/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pre-commit install
