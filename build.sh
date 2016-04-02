#!/bin/bash

echo -e 'Building Package\n';
cd django-pa;
python setup.py sdist;
echo -e 'Finish Building Package\n';
