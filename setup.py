import setuptools
import setuptools_scm


def get_my_version():
    import os

    # https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html#git-environment-variables
    version = os.environ.get("GIT_DESCRIBE_TAG")
    if version is not None:
        build_string = os.environ.get("GIT_BUILD_STR")
        if len((build_string or "").strip()) > 0:
            version += f"+{build_string}"
    else:
        version = setuptools_scm.get_version()
    return version


setuptools.setup(
    version=get_my_version(),
)
