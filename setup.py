import setuptools
import setuptools_scm


def get_my_version():
    import os

    # https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html#git-environment-variables
    version = os.environ.get("git_describe")
    if version is None:
        version = setuptools_scm.get_version()
    return version


setuptools.setup(
    version=get_my_version(),
)
