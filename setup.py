from setuptools import find_packages, setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="barrentix",
    version="0.0.1",
    description="A modern framework inspired on Laravel, with elegant syntax for building large, scalable and complex web APIs, web applications and console applications.",  # noqa
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fbarrento/barrentix",
    author="Francisco Barrento",
    author_email="francisco.barrento@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "SQLAlchemy==2.0.15",
        "psycopg2-binary==2.9.6",
        "PyMySQL==1.0.3",
        "pyodbc==4.0.39",
        "omegaconf==2.3.0",
        "importlib==1.0.4"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "twine>=4.0.2"
        ],
    },
    python_requires=">=3.10",
)
