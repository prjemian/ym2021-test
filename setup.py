import configparser
import setuptools
from setuptools_scm import get_version

setuptools.setup()

# adapter for use in conda's meta.yaml file
conda_meta = dict(version=get_version())
_setup_cfg = configparser.ConfigParser()
_setup_cfg.read("setup.cfg")
for _key in "description keywords license name url".split():
    conda_meta[_key] = _setup_cfg.get("metadata", _key)

del _key
del _setup_cfg
