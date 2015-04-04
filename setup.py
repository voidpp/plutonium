from setuptools import setup, find_packages

setup(
    name = "Plutonium",
    version = '1.0',
    install_requires = [
        "SQLAlchemy >= 0.9.8",
        "alembic == 0.7.4",
        "python-jsonrpc == 0.6.1",
    ],
    packages = find_packages(),
    include_package_data = True,
    scripts = [
        'bin/plutonium',
        'bin/plutonium_starter',
    ]
)

