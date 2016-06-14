"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/Rambatino/CHAID
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='CHAID',
    version='1.0',
    description='A CHAID tree building algorithm',
    long_description='CHAID enables the building of decision trees using the Chi-Squared test for significance. As it is built on numpy dataframes, it works well with pandas.',
    url='https://github.com/Rambatino/CHAID',
    author='Mark Ramotowski',
    author_email='mark.tint.ramotowski@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='CHAID pandas numpy scipy statistics statistical analysis',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['numpy', 'scipy'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    data_files=[('my_data', ['example_files/CHAID.csv'])],
)