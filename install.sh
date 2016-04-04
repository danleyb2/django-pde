#!/usr/bin/env bash

echo -e '[*]Uninstalling Package\n';
echo y|sudo -H pip uninstall django-pa
echo -e '[*]Finnish Uninstalling Package\n';

echo -e '[*]Installing Package\n';

sudo -H python "${PROJECT_PATH}django-pa/setup.py" install;
echo -e '[*]Finish Installing Package\n';