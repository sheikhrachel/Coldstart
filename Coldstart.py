# cli.py
import click
import sys
sys.path.append('/path/to/application/app/folder')
from validate_responses import create_project_validation
from logo import present_logo


@click.command()
def Coldstart():
    click.clear()
    present_logo()
    create_project_validation()


# f=(open(filename), 'w+')


if __name__ == "__main__":
    main()
