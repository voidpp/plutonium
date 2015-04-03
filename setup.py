from setuptools import setup, find_packages

setup(
    name = "Plutonium",
    version = '0.4',
    install_requires = [
        "SQLAlchemy >= 0.9.8"
    ],
    packages = find_packages(),
    scripts = [
        'bin/plutonium',
        'bin/plutonium_starter',
    ]
)

