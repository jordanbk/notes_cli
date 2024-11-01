import click
from notes import crud

@click.group()
def cli() -> None:
    print("I'm working!")

cli.add_command(crud.create)


