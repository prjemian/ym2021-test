try:
    from setuptools_scm import get_version

    __version__ = get_version()
except (LookupError, ModuleNotFoundError):
    from importlib.metadata import version

    __version__ = version("pyRestTable")
