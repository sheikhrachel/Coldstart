# license_determination.py
import click
from licenses import Apache_str, GNUGPL3_str, MIT_str


# Create license file for project
def license_determination(license_type: str):
    if license_type == "none":
        click.echo("No license specified.  Skipping step.")
    elif license_type == "Apache":
        click.echo("Creating Apache license file in project root")
        f = open("LICENSE.md", "w+")
        f.write(Apache_str)
        f.close()
    elif license_type == "GNUGPL3":
        click.echo("Creating GNU General Public v3.0 license file in project root")
        f = open("LICENSE.md", "w+")
        f.write(GNUGPL3_str)
        f.close()
    elif license_type == "MIT":
        click.echo("Creating MIT license file in project root")
        f = open("LICENSE.md", "w+")
        f.write(MIT_str)
        f.close()
    else:
        click.echo("License type not yet supported.  Skipping step.")
