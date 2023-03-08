"""
Sets up pre-commit
"""
from datetime import datetime
from setuptools import setup, find_packages

PACKAGES = find_packages(exclude=["test*", "tests*", "testing*"])

PROJECT_NAME = "pre-commit-coding-standards"
PROJECT_PACKAGE_NAME = "pre-commit-coding-standards"
PROJECT_LICENSE = "MIT"
PROJECT_AUTHOR = "@johnsondnz"
PROJECT_COPYRIGHT = f"2018-{datetime.now().year}"
PROJECT_URL = "https://github.com/johnsondnz/pre-commit-coding-standards"
PROJECT_EMAIL = "donaldjohnsond.nz@gmail.com"
PROJECT_VERSION = "1.1.2"

REQUIRES = [
    "flake8==3.9.2",
    "six",
    "typing",
    "PyYAML>=5.1.2",
    "black==21.9b0",
    "GitPython==3.1.30",
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    url=PROJECT_URL,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=">=3.5",
    entry_points={"console_scripts": ["coding-standards = hooks.coding_standards:main"]},
)
