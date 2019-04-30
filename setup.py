from setuptools import find_packages, setup

setup(
    name="se",
    version="0.1.0",

    packages=find_packages(),

    entry_points={
        "console_scripts": [
            "ssam = ssam:main",
        ],
    },

    install_requires=["docopt"],
)
