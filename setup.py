from typing import List

from setuptools import find_packages
from setuptools import setup


def get_install_requires(path: str) -> List[str]:
    with open(path, mode="r") as f:
        return [line.strip() for line in f.readlines()]


setup(
    name="power-consumption",
    version="0.1.0",
    package_dir={"": "src"},
    python_requires=">=3.8.8",
    install_requires=get_install_requires("requirements.txt"),
    package_data={"power-consumption": ["power-consumption/config.yaml"]},
)
