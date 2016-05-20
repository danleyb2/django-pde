import os
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='django-{{options.app_name}}',
      version='{{options.version}}',
      author='',
      author_email='',
      description='{{ options.app_name }} description',
      long_description=open('README.rst').read(),
      license='LICENSE.txt',
      keywords="",

      # package source directory
      #package_dir={'': 'src'},
      packages=find_packages()
{% if options.with_cli %}
{% set module_name = options.package_name.lower() %}
    # configure the default command line entry point.
    , entry_points={
          'console_scripts': [
              '{{module_name}} = bin.{{module_name}}:main',
          ]
      }
{% endif %}
{% if options.with_tests %}
    # configure the default test suite
    , test_suite='tests.suite'
{% endif %}
)
