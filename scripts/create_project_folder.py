# cli.py
import click
import os


def create_project_validation():
    current_path = os.getcwd()
    click.echo('The current working directory is ', current_path)
    click.echo('Would you like to create a new project in this directory? [Y/n] ', nl=False)
# target_path = click.echo('Where would you like to create this project at: ', type=str)
    project_name = click.echo('What would you like to name this project: ', type=str)
    project_path = current_path + '/' + project_name
    try:
        os.mkdir(project_path)
    except OSError:
        click.echo('that path won\'t work!')
    else:
        click.echo('Project created at ', project_path)
        click.echo('Changing current working directory to project directory')
