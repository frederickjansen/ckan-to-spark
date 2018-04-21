from setuptools import setup
from io import open
import re

# Parse the version from the module without importing
with open('ckan_to_spark/__init__.py', 'r') as f:
    version = re.search('__version__ = \'(.*?)\'', f.read()).group(1)

# Retrieve dependencies
with open('requirements.txt', 'r') as f:
    reqs = f.readlines()
with open('test-requirements.txt', 'r') as f:
    test_reqs = f.readlines()

# Retrieve readme
with open('README.rst', 'r') as f:
    long_desc = f.read()

setup(
    name='prequest',
    version=version,
    description='Convert CKAN data portals to Spark with Parquet on HDFS.',
    long_description=long_desc,
    author='Frederick Jansen',
    author_email='fjansen@bu.edu',
    url='https://github.com/frederickjansen/ckan-to-spark',
    packages=['ckan-to-spark'],
    install_requires=reqs,
    tests_require=test_reqs,
    test_suite='nose.collector',
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ),
)
