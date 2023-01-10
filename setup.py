from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="json-to-files",
    description="Create separate files on disk based on a JSON object",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/json-to-files",
    project_urls={
        "Issues": "https://github.com/simonw/json-to-files/issues",
        "CI": "https://github.com/simonw/json-to-files/actions",
        "Changelog": "https://github.com/simonw/json-to-files/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["json_to_files"],
    entry_points="""
        [console_scripts]
        json-to-files=json_to_files.cli:cli
    """,
    install_requires=["click"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
