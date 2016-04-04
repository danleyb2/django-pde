#!/bin/bash

echo -e 'Uninstalling Package\n';
sudo -H echo y|pip uninstall pa
echo -e 'Finnish Uninstalling Package\n';

echo -e 'Installing Package\n';

sudo -H python /home/ubuntu/workspace/django-pa/setup.py install;
echo -e 'Finish Installing app\n';