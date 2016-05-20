import os
from setuptools import setup
import setuptools
import pde
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pde',
    version=pde.__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['jinja2','sh'],
    license='GNU License',
    description='Django app that can be used to easily manage development of other django packages',
    long_description=README,
    url='https://github.com/danleyb2/django-pde/wiki',
    author=pde.__author__,
    author_email='ndieksman@gmail.com',
    classifiers=[
        'Development Status :: 0.01 - Beta ',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
