# exit_test.py
import click
import os


# Delete working directory from file system for debugging
def exit_test(current_path: str, project_path: str):
    click.pause()
    old_path: str = current_path
    current_path: str = project_path
    click.echo('Current working directory is %s' % current_path)
    os.chdir(old_path)
    click.echo('Current working directory is %s' % old_path)
    os.rmdir(current_path)
    click.echo('%s deleted!' % current_path)
