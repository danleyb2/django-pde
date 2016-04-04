#!/usr/bin/env bash


export PROJECT_PATH='/home/ubuntu/workspace/'

echo '[*]Start redeploy';

source "${PROJECT_PATH}env34/bin/activate";

source "${PROJECT_PATH}cp.sh";
source "${PROJECT_PATH}build.sh";
source "${PROJECT_PATH}install.sh";

deactivate;

echo '[*]End redeploy';