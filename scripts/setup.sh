#!/bin/bash

python3 -m venv work
source work/bin/activate
autotest
main
pip install -r requirements.txt
pre-commit install
