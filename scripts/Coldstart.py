# cli.py
import click
from validate_responses import create_project_validation
from logo import present_logo


@click.command()
def main():
    click.clear()
    present_logo()
    create_project_validation()


# f=(open(filename), 'w+')


if __name__ == "__main__":
    main()
