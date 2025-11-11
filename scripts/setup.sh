#!/bin/bash

python3 -m venv work
source work/bin/activate
pip install -r requirements.txt
pre-commit install
