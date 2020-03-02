# Coldstart.py #from logo import present_logo
import click
import os
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from create_readme import create_readme
from license_determination import license_determination
from language_determination import language_determination
from repo_creation import repo_creation
from exit_test import exit_test


@click.group(chain=True)
@click.pass_context
def cli(ctx):
    init(strip=not sys.stdout.isatty())
    pyfig_text = "Coldstart"
    click.clear()
    cprint(figlet_format(pyfig_text, font="standard"), "blue")


@cli.command("project")
@click.option("-p", required=True, type=str)
@click.option("-l", type=str)
@click.option("-lang", type=str)
@click.option("-g", type=str)
def create_project(p, l, lang, g):
    click.echo("Creating Project: [" + p + "]")
    os.mkdir(p)
    os.chdir(p)
    create_readme(p)
    license_determination(l)
    language_determination(p, lang)
    repo_creation(g)


@cli.command("kill")
@click.option("-p", required=True, type=str)
def kill(p):
    exit_test(p)


if __name__ == "__main__":
    cli()
