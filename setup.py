"""
Setup.py for gh
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='gh',
    version='0.0.2',
    description='',
    long_description='A CLI to open Github project in a browser',
    url='https://github.com/danielwhatmuff/gh',
    author='Daniel Whatmuff',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='github cli open repo commandline browser',
    py_modules=["gh"],
    install_requires=['gitpython'],
    scripts=['bin/gh'],
)
