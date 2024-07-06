from setuptools import setup, find_packages

VERSION = '0.0.1'


if __name__ == '__main__':

    with open("README.md", 'r') as doc:
        long_description = doc.read()

    with open("requirements.txt", 'r') as req:
        requirements = req.readlines()

    setup(
        name="isn",
        description="A library to test trading strategies on historical data, or live data",
        long_description=long_description,
        version=VERSION,
        classifiers=[
            "Programming Language :: Python :: 3.10"
        ],
        author="Pertingens",
        install_requires=requirements,
        packages=find_packages(
            include=[
                'isn_project*'
            ],
            exclude=[
                '*tests*'
            ]
        ),
        extras_require={
            "dev": [
                "tox",
                "sphinx"
            ]
        },
        package_data={'': ['*.json', '*.yml']},
    )