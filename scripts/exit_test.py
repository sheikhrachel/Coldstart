# exit_test.py
import click
import os
import shutil


# Delete working directory from file system for debugging
def exit_test(project_name: str):
    os.chdir(project_name)
    project_path = os.getcwd()
    os.chdir(r'..')
    click.echo('Deleting Project: [' + project_name + ']')
    shutil.rmtree(project_path)
    click.echo('Project [' + project_name + '] deleted!')
