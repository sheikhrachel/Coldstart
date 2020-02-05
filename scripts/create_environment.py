# create_environment.py
import click
import os
import sys
# from python_setup import python_setup


# Navigate to correct setup script based on language
def create_environment():
    pass


# Determine which language to setup environment in
def determine_language():
    pass


# Handle incorrect inputs for determine_language()
def determine_language_no_prompt():
    pass


# Handle init git repo for project from user provided git remote
def init_git():
    click.echo('What is your GitHub remote url: ', nl=False)
    for line in sys.stdin:
        url: str = line.rstrip()
        break
    git_remote = url
    os.system('git init')
    click.echo('initialised git')
    os.system('git add .')
    click.echo('repo staged')
    os.system('git commit -m \'init\'')
    click.echo('repo committed')
    os.system('git remote add origin %s' % git_remote)
    click.echo('git remote configured')
    os.system('git push -u origin master')
    click.echo('git repo pushed!')
