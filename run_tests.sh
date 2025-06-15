#!/bin/bash

""" Activate the virtual environment"""
source venv/bin/activate

""" Run the test suite"""
pytest test_app.py

""" Check the exit status of pytest"""
if [ $? -eq 0 ]; then
    echo "COngratulation: All tests passed."
    exit 0
else
    echo "Error: Some tests failed."
    exit 1
fi
