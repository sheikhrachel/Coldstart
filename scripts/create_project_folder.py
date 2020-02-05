# cli.py
import click
import os
import sys


def create_project_folder():
    project_path = set_new_project_name()

    click.echo('Project created at %s' % project_path)
    click.echo('Changing current working directory to project directory')
    try:
        os.chdir(project_path)
    except OSError:
        click.echo('that path won\'t work!')


def determine_correct_path():
    current_path: str = os.getcwd()
    click.echo('Current working directory is %s' % current_path)
    click.echo('Would you like to create a new project in this directory? [Y/n]: ', nl=False)
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo(' ')
        return current_path
    elif c == 'n':
        click.echo(c)
        click.echo(' ')
        set_new_project_path()
        current_path: str = os.getcwd()
        click.echo('New working directory is %s' % current_path)
        return current_path
    else:
        determine_correct_path_no_prompt()


def determine_correct_path_no_prompt():
    current_path: str = os.getcwd()
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo(' ')
        return current_path
    elif c == 'n':
        click.echo(c)
        click.echo(' ')
        set_new_project_path()
        target_path: str = os.getcwd()
        current_path: str = target_path
        click.echo('New working directory is %s' % current_path)
        return current_path
    else:
        determine_correct_path_no_prompt()


def set_new_project_path():
    click.echo('What directory would you like to create a new project in: ', nl=False)
    for line in sys.stdin:
        new_directory: str = line.rstrip()
        break
    try:
        os.chdir(new_directory)
    except OSError:
        click.echo('%s path is not valid' % new_directory)
        set_new_project_path()


def set_new_project_name():
    target_path: str = determine_correct_path()
    click.echo('What would you like to name this project: ', nl=False)
    for line in sys.stdin:
        project_name: str = line.rstrip()
        break
    project_path: str = os.path.join(target_path, project_name)
    try:
        os.mkdir(project_path)
        return project_path
    except OSError:
        click.echo('that project already exists!')
        click.echo(' ')
        set_new_project_name()
