"""Setuptools setup file"""

from setuptools import setup

# Ridiculous as it may seem, we need to import multiprocessing and logging here
# in order to get tests to pass smoothly on python 2.7.
import multiprocessing
import logging


def get_description(fname='README.rst'):
    # Adapted from PEAK-Rules' setup.py
    # Get our long description from the documentation
    f = file(fname)
    lines = []
    for line in f:
        if not line.strip():
            break     # skip to first blank line
    for line in f:
        if line.startswith('Documentation contents'):
            break     # read to "Documentation contents..."
        lines.append(line)
    f.close()
    return ''.join(lines)


setup(
    name='macchiato',
    version='0.0.1',
    description="Python to javascript compilation",
    long_description=get_description(),
    install_requires=[
    ],
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    license='LGPLv2+',
    packages=['macchiato'],
    # TODO -- include console-script
    entry_points="""
    """,
    zip_safe=False,
    include_package_data=True,
)
