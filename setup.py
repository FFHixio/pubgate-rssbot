import os, re
from setuptools import setup, find_packages

reqs_path = "requirements.txt"
with open(reqs_path) as reqs_file:
    reqs = reqs_file.read().splitlines()

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="rssbot",
    description="Extension for PubGate, federates rss-feeds",
    author="autogestion",
    author_email="",
    url="https://github.com/autogestion/pubgate-rssbot",
    version=get_version('rssbot'),
    packages=find_packages(),
    install_requires=reqs,
    license="BSD 3-Clause",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Framework :: Sanic",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ),
    platforms="Python 3.6 and later."
)