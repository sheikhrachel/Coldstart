# logo.py
import click
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from start_coldstart import validate_create_project

init(strip=not sys.stdout.isatty())
pyfig_text = 'Coldstart'


# Version option flag
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Coldstart version 0.0.1')
    ctx.exit()


# Clear terminal and display 'Coldstart' logo at top of screen
@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def present_logo():
    click.clear()
    cprint(figlet_format(pyfig_text, font='standard'), 'blue')
    validate_create_project()
