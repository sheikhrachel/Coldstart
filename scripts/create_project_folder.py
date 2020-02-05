# create_project_folder.py
import click
import os
import sys
from exit_test import exit_test
from create_environment import init_git


# Create new project and set working directory to project location
def create_project_folder():
    project_details_dict = set_new_project_name()
    click.echo('%s created at %s' % (project_details_dict['project name'], project_details_dict['project path']))
    click.echo('Changing current working directory to project directory')
    os.chdir(project_details_dict['project path'])
    init_git()
    exit_test(project_details_dict['project path'])


# Validate current working directory destination for project directory
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


# Handle incorrect inputs for determine_correct_path()
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


# Set new working directory destination for project directory
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


# Set new project name to create project directory
def set_new_project_name():
    target_path: str = determine_correct_path()
    project_details_dict: dict = {'project name': '', 'project path': ''}
    click.echo('What would you like to name this project: ', nl=False)
    for line in sys.stdin:
        project_name: str = line.rstrip()
        break
    project_details_dict['project name']: str = project_name
    project_details_dict['project path']: str = os.path.join(target_path, project_details_dict['project name'])
    try:
        os.mkdir(project_details_dict['project path'])
        return project_details_dict
    except OSError:
        click.echo('That project already exists!')
        click.echo(' ')
        set_new_project_name()
