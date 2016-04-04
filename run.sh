#!/usr/bin/env bash


source env34/bin/activate;
cd testing_prj;
python manage.py migrate;
python manage.py runserver $IP:$PORT;