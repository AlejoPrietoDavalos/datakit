from setuptools import setup, find_packages

setup(
    name = "datatools",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = [
        "numpy==1.26.0",
        "pydantic==2.4.2",
        "matplotlib==3.8.0",
        "rasterio==1.3.8",
    ],
)
