#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Internet",
    "Topic :: Utilities",
]

with open("README.rst") as file_readme:
    readme = file_readme.read()

with open("HISTORY.rst") as file_history:
    history = file_history.read()

setup(
    name="retrying",
    version="1.4.1-dev",
    description="Retrying",
    long_description=readme + "\n\n" + history,
    author="Greg Roodt",
    license="Apache 2.0",
    url="https://github.com/groodt/retrying",
    classifiers=CLASSIFIERS,
    keywords="decorator decorators retry retrying exception exponential backoff",
    py_modules=["retrying"],
    test_suite="test_retrying",
    python_requires=">=3.6",
)
