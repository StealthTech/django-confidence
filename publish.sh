#!/bin/bash

source env/bin/activate
cd build/django-conf/dist

if [ "$2" == "dev" ]; then
	twine upload --repository-url https://test.pypi.org/legacy/ "$1.tar.gz"
elif [ "$2" == "prod" ]; then
	echo "prod"
fi
