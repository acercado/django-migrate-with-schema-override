import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-migrate-with-schema-override',
    version=0.1,
    packages=[django_migrate_with_schema_override],
    include_package_data=True,
    license='MIT',
    description='Override migrate command not to trip on tables with schema name provided via db_tables.',
    long_description=README,
    author='Ariel Cercado',
    author_email='ariel.cercado@gmail.com',
    url='http://github.com/acercado/django_migrate_with_schema_override',
    classifiers=[
        'Environment :: Web Development',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
)
