#!/bin/bash

source "env/bin/activate"
cd build/dist

PACKAGE_NAME="django-confidence"

if [ "$#" -ne 2 ]; then
    echo "Usage: ./publish.sh package (dev || prod)"
    echo "Example: ./publish.sh $PACKAGE_NAME-1.0 dev"
    exit 1
fi

if [ "$2" == "dev" ]; then
	twine upload --repository-url https://test.pypi.org/legacy/ "$1.tar.gz"
elif [ "$2" == "prod" ]; then
	twine upload "$1.tar.gz"
fi
