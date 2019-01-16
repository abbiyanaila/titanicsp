import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="titanicsp",
    version="0.1",
    author="Desi Ratna Ningsih",
    author_email="abbiyanaila@gmail.com",
    description="Titanic Survived Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abbiyanaila/titanicsp",
    packages=setuptools.find_packages(),
    classifiers=""
)