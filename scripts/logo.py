# cli.py
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())
pyfig_text = 'Coldstart'


def present_logo():
    cprint(figlet_format(pyfig_text, font='standard'), 'blue') 