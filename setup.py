import os
import sys
import re

name = "mort"

if sys.version_info < (3,4):
    raise Exception("Requires Python3.4+")

from setuptools import setup, find_packages
try:
    with open('README.md') as fh:
        long_description = fh.read()
except FileNotFoundError:
    # This isn't working on py34 on travis-ci
    # It's not important so ignore for now
    long_description = ""

def _get_version():
    VERSIONFILE="{name}/__init__.py".format(name=name)
    with open(VERSIONFILE) as fh:
        verstrline = fh.read()
    VSRE = r"^__version__ *= *(.*)"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1).strip("\"\'")
    else:
        raise Exception("Unable to find version string in %s." % (VERSIONFILE,))
    return verstr

version = _get_version()
setup(name=name,
      version=version,
      description='Debug on exception',
      author='Bryce Guinta',
      author_email='contact@bryceguinta.me',
      long_description=long_description,
      packages=[name],
      license='MIT',
      entry_points={'console_scripts': ['mort = mort:main']},
      zip_safe=True,
      classifiers=[
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
      ],
      long_description_content_type='text/markdown',
      url = 'https://github.com/brycepg/mort',
      install_requires = [
          'mand',
      ]
     )
