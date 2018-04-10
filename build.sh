#!/bin/bash

PROJECT_NAME="confidence"

rm -r "build/$PROJECT_NAME"
cp -r "project/$PROJECT_NAME" build
source "env/bin/activate"
cd build
python setup.py sdist
