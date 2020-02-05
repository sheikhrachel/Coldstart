import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Coldstart-sheikhisaac",
    version="0.0.1",
    author="Isaac Sheikh",
    author_email="sheikhisaac@example.com",
    description="cli tool for rapid project bootstrapping",
    long_description='Coldstart is a Python cli tool built with click to quickly create a development environment for \
                        your next project',
    long_description_content_type="text/markdown",
    url="https://github.com/sheikhisaac/Coldstart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Mac",
    ],
    python_requires='>=3.6',
)
