# validate_responses.py
import click


# Check if user wants to create a new project or not
def validate_create_project():
    from create_project_folder import create_project_folder
    click.echo('Would you like to create a new project? [Y/n]: ', nl=False)
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo(' ')
        create_project_folder()
    elif c == 'n':
        click.echo(c)
        click.echo('Abort!')
    else:
        validate_create_project_no_prompt()


# Handle incorrect inputs for validate_create_project()
def validate_create_project_no_prompt():
    c = click.getchar()
    if c == 'y':
        click.echo(c)
        click.echo(' ')
    elif c == 'n':
        click.echo(c)
        click.echo('Abort!')
    else:
        validate_create_project_no_prompt()
