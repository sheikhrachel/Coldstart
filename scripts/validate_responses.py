# cli.py
import click


def create_project_validation():
    from create_project_folder import create_project_folder
    click.echo('Would you like to create a new project? [Y/n]: ', nl=False)
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo(' ')
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
        click.echo(' ')
    elif c == 'n':
        click.echo(c)
        click.echo('Abort!')
    else:
        validate_switch_no_prompt()
