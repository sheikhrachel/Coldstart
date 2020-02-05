# logo.py
import click
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())
pyfig_text = 'Coldstart'


# Clear terminal and display 'Coldstart' logo at top of screen
@click.command()
def present_logo():
    click.clear()
    cprint(figlet_format(pyfig_text, font='standard'), 'blue') 
