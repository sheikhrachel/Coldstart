# Coldstart

Coldstart is a Python cli tool built with click to quickly create a development environment for your next project

## Features
- Builds configured with Poetry

- Sets up git connections based on provided repository remote

- Git hooks configured with Pre-Commit

- File directory navigation to create projects from anywhere within filesystem

- Current environment language support: Python3

## Prerequisites

Ensure you are running a Python version >= 3.6

```zsh
$ python3 --version # returns 'Python 3.7.1' or a version >= 'Python 3.6'
```

Use pip3 to install the Coldstart package

```zsh
$ pip3 install Coldstart
```

Validate Coldstart installation with --version

```zsh
$ Coldstart --version # returns 'Coldstart version 0.0.1'
```

## Usage

```zsh
$ Coldstart # Starts the Coldstart project creation flow
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