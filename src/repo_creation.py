# repo_creation.py
import click
import os


# Handle init git repo for project from user provided git remote
def repo_creation(g: str):
    git_remote = g
    os.system("git init")
    click.echo("initialised git")
    os.system("git add .")
    click.echo("repo staged")
    os.system("git commit -m 'init'")
    click.echo("repo committed")
    os.system("git remote add origin %s" % git_remote)
    click.echo("git remote configured")
    os.system("git push -u origin master")
    click.echo("git repo pushed!")
