import setuptools
import setuptools_scm


def get_my_version():
    import os

    # https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html#git-environment-variables
    version = os.environ.get("GIT_DESCRIBE")
    if version is None:
        version = setuptools_scm.get_version()
    else:
        parts = version.split("-")
        version = parts[0]
        if len(parts) > 1:
            version += f".dev{parts[1]}"
        if len(parts) > 2:
            version += f"+{parts[2].split('.')[0]}"
    return version


setuptools.setup(
    version=get_my_version(),
)
