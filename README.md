![PyPI](https://img.shields.io/pypi/v/mort.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mort.svg)
[![GitHub license](https://img.shields.io/github/license/brycepg/mort.svg)](https://github.com/brycepg/mort/blob/master/LICENSE)


Start debugging on exception. No code changes necessary

# Installation

    pip install mort

# Usage

Invoke mort on any file or module you'd like to debug

    mort file/to/debug.py

pdb will be invoked when an exception occurs.

## Use with an entry point

You can use mort to debug an exception in a python program if it has a python entry point:

    mort "$(which <your-entry-point>) [possible arguments]"
