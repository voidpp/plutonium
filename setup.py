from setuptools import setup, find_packages

setup(
    name="Plutonium",
    version='0.2',
    install_requires=[
        "SQLAlchemy >= 0.9.8"
    ],
    packages=find_packages(),
    scripts=['bin/plutonium']
)

