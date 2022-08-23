import configparser
import setuptools
from setuptools_scm import get_version

setuptools.setup()

# adapters for use in conda's meta.yaml file
_setup_cfg = configparser.ConfigParser()
_setup_cfg.read("setup.cfg")

__pkg_description__ = _setup_cfg.get("metadata", "description")
__pkg_keywords__ = _setup_cfg.get("metadata", "keywords")
__pkg_license__ = _setup_cfg.get("metadata", "license")
__pkg_name__ = _setup_cfg.get("metadata", "name")
__pkg_url__ = _setup_cfg.get("metadata", "url")
__pkg_version__ = get_version()

del _setup_cfg
del get_version
