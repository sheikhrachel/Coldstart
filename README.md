# Coldstart

Coldstart is a Python cli tool built with click to quickly create a development environment for your next project

## Features
- Builds configured via Travis CI/CD

- Git hooks configured with Pre-Commit

- File directory navigation to create projects from anywhere within filesystem

- Multiple language support: Python3, Ruby, C++

## Prerequisites

Ensure you are running Python 3.7.1

```zsh
$ python3 --version # returns 'Python 3.7.1'
```

Use pipenv to install all required pip3 packages from Pipfile and create virtual environment

```zsh
$ pipenv install
```

Use pipenv to access functions

```zsh
$ pipenv shell
```

Set up git hooks for pre-commit checks notated in .pre-commit-config.yaml

```zsh
$ pre-commit install
```

## Usage

```zsh
$ python3 Coldstart.py
```

Run the unit tests

```zsh
$ pytest -v
```

## Contact Info

```python
self.name = 'Isaac Sheikh'
self.email = 'sheikhisaac@gmail.com'
self.phone = '571-315-1881'
```

## Potential Next Steps

- Implement tab completion for directory lookup
- Add additional language support