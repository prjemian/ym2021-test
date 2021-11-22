import os
import setuptools

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name = "ym2021_prj",
    version = "0.0.4",
    author = "Pete R. Jemian",
    author_email = "prjemian@gmail.com",
    description = ("Repository to test GitHub Actions Workflows."),
    license = "CC0 1.0 Universal",
    keywords = "Python test repository",
    url = "https://github.com/prjemian/ym2021_prj",
    packages=setuptools.find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: CC0 1.0 Universal",
    ],
)