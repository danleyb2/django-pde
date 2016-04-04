#!/usr/bin/env bash

echo -e '[*]Building Package\n';
python "${PROJECT_PATH}django-pa/setup.py" sdist;
echo -e '[*]Finish Building Package\n';
