from setuptools import setup, find_packages

setup(
    name="buffalo",
    version=0.01,
    url="https://github.com/lukas-hager/buffalo",
    author="Lukas Hager",
    author_email="lghhager@uw.edu",
    install_requires=["numpy", "xarray"],
    packages=find_packages(),
)