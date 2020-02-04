# cli.py
import click
from create_project_folder import create_project_folder


def create_project_validation():
    click.echo('Would you like to create a new project? [Y/n] ', nl=False)
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo('We will go on')
        create_project_folder()
    elif c == 'n':
        click.echo(c)
        click.echo('Abort!')
    else:
        validate_switch_no_prompt()


def validate_switch_no_prompt():
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo('We will go on')
    elif c == 'n':
        click.echo(c)
        click.echo('Abort!')
    else:
        validate_switch_no_prompt()