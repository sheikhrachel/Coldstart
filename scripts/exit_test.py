# exit_test.py
import click
import os
import shutil


# Delete working directory from file system for debugging
def exit_test(project_path: str):
    click.pause()
    current_path: str = project_path
    click.echo('Current working directory is %s' % current_path)
    os.chdir(r'..')
    click.echo('Current working directory is %s' % os.getcwd())
    shutil.rmtree(current_path)
    click.echo('%s deleted!' % current_path)
