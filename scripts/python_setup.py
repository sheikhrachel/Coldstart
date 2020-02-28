# python_setup.py
# import click
import os


# create python development: create pre-commit config file,
# create pipfile, create tox.ini file, create travis.yml file,
# create main.py file in src folder, create api_key.py file,
# create test_main.py file in test folder
def python_setup(project_name: str):
    # gitignore setup
    f = open(".gitignore", "w+")
    f.write(gitignore_str)
    f.close()
    # Pipfile setup
    f = open("Pipfile", "w+")
    f.write(pipfile_str)
    f.close()
    # pre-commit config
    f = open(".pre-commit-config.yaml", "w+")
    f.write(precommit_str)
    f.close()
    # tox.ini setup
    f = open("tox.ini", "w+")
    f.write(tox_str)
    f.close()
    # travis setup
    f = open(".travis.yml", "w+")
    f.write(travis_str)
    f.close()

    # src folder files
    os.mkdir("src")
    os.chdir("src")
    # main project py file
    f = open(project_name + ".py", "w+")
    f.close()
    # api key file
    f = open("api_key.py", "w+")
    f.close()
    # gitignore for src directory
    f = open(".gitignore", "w+")
    f.write(gitignoresrc_str)
    f.close()
    os.chdir(r"..")

    # test folder files
    os.mkdir("tests")
    os.chdir("tests")
    f = open("test_" + project_name + ".py", "w+")
    f.write("import pytest")
    f.close()
    os.chdir(r"..")


gitignore_str = """
.gitattributes
__pycache__
.pytest_cache
"""

gitignoresrc_str = """
api_key.py
"""

pipfile_str = """
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
requests = "*"
pytest = "*"
pre-commit = "*"
black = "*"

[requires]
python_version = "3.7"

[pipenv]
allow_prereleases = true
"""

precommit_str = """
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.4.0  # Use the ref you want to point at
    hooks:
    -   id: trailing-whitespace
    -   id: check-ast
    -   id: check-case-conflict
    -   id: check-yaml
    -   id: pretty-format-json
        args: ["--autofix"]

-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.8

-   repo: local
    hooks:
    -   id: python-bandit-vulnerability-check
        name: bandit
        entry: bandit
        args: ['--ini', 'tox.ini', '-r', 'consoleme']
        language: system
        pass_filenames: false
    -   id: tests
        name: run tests
        entry: pytest -v
        language: system
        types: [python]
        stages: [push]
"""

travis_str = """
language: python
python:
  - "3.8"
install:
  - pipenv install
script:
  - pipenv run pytest -v
"""

tox_str = """
[tox]
envlist = py37
"""
