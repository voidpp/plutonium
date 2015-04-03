from setuptools import setup, find_packages

setup(
    name = "Plutonium",
    version = '0.4',
    install_requires = [
        "SQLAlchemy >= 0.9.8",
        "alembic == 0.7.4",
    ],
    packages = find_packages(),
    include_package_data = True,
    scripts = [
        'bin/plutonium',
        'bin/plutonium_starter',
    ]
)

