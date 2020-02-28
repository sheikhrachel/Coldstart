# license_determination.py
import click
from python_setup import python_setup


def language_determination(project_name: str, language: str):
    if language == 'none':
        click.echo('No Language specified.  Skipping step.')
    elif language == 'python':
        python_setup(project_name)
    else:
        click.echo('Language not supported yet.  Skipping step')
