#!/bin/bash

echo 'Start redeploy';

source /home/ubuntu/workspace/env34/bin/activate;

source /home/ubuntu/workspace/cp.sh;
source /home/ubuntu/workspace/build.sh;
source /home/ubuntu/workspace/install.sh;

deactivate;

echo 'End redeploy';