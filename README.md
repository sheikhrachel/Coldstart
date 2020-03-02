# Coldstart
[![Build status](https://travis-ci.com/sheikhisaac/Coldstart.svg?token=zsGPkD9bv7zhqvJzsjQU&branch=master)](https://travis-ci.org/sheikhisaac)

Coldstart is a Python cli tool built with click to quickly create a development environment for your next project

## Features
- Builds configured with Travis with build tag bootstrap in readme.md file

- Gitignores pulled from Github bootstrap examples

- Sets up git connections based on provided repository remote

- Git hooks configured with Pre-Commit

- Current environment language support: Python3

- Current License support: Apache, GNUGPL v3.0, MIT

## Prerequisites

Ensure you are running a Python version >= 3.6

```zsh
$ python3 --version # returns 'Python 3.7.1' or a version >= 'Python 3.6'
```

## Usage

Run in terminal from the src file (I will eventually publish this project up to pip for install/run directly)

```zsh
# Project creation
$ Coldstart project -p'project name' -l 'license selection' -lang 'language selection' -g 'github repo link'

# Project deletion
$ Coldstart project -p'project name'
```

## Contact Info

```python
self.name = 'Isaac Sheikh'
self.email = 'sheikhisaac@gmail.com'
self.phone = '571-315-1881'
```