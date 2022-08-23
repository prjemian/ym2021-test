import setuptools
from setuptools_scm import get_version

# adapters for use in conda's meta.yaml file
version = get_version()
del get_version

setuptools.setup()
