#!/bin/bash

rm -r build/django-conf/conf
cp -r django_conf/conf build/django-conf
source env/bin/activate
cd build/django-conf
python setup.py sdist

