# Coldstart
[![Build status](https://travis-ci.com/sheikhisaac/Coldstart.svg?token=zsGPkD9bv7zhqvJzsjQU&branch=master)](https://travis-ci.org/sheikhisaac)

Coldstart is a Python cli tool built with click to quickly create a development environment for your next project

## Features
- Builds configured with Travis

- Sets up git connections based on provided repository remote

- Git hooks configured with Pre-Commit

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
# Starts the Coldstart project creation flow step-by-step
$ Coldstart --verbose
$ Coldstart -v

# One-liner for project creation
$ Coldstart --projectName (required) 'project name' --projectDirectory (optional) '/directory/path' --gitRemote (optional) 'git remote url' --environment (optional) 'dev language' --license (optional) 'license'

# Short-mode one-liner for project creation
$ Coldstart -pn (required) 'project name' -pd (optional) '/directory/path' -gr (optional) 'git remote url' -e (optional) 'dev language' -l (optional) 'license'
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