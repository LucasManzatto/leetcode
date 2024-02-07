from setuptools import find_packages, setup

setup(
    name="leetcode",
    version="1.0",
    description="Leetcode problems with data structures",
    author="Lucas",
    author_email="",
    packages=find_packages(exclude=("tests", "docs")),
)
