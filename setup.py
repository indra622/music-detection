import setuptools

requirements = [
    "setuptools>=47.1.1",
]

setuptools.setup(
    name="Shazam-air",
    version="0.0.1",
    author="asdf",
    packages=setuptools.find_packages(include=["src*"]),
    install_requires=requirements,

    python_requires='>=3.6',
)