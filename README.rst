
.. image:: https://badge.fury.io/py/django-pde.svg
    :target: https://badge.fury.io/py/django-pde

===========
quick setup
===========

.. code-block:: sh

    pip install django-pde;
    pip install https://github.com/danleyb2/django-pde/archive/master.zip # from src

    django-admin startproject myproject;
    cd myproject;
    python manage.py startapp myapp;

    # add pde to INSTALLED_APPS

    python manage.py pde -n myapp;   #creates a new package for myapp
        
