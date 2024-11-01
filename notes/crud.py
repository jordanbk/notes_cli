import click
import json
from datetime import datetime
from pathlib import Path

@click.command()
@click.argument("title")
@click.option("--content")
@click.option("--tags")
def create(title:str, content:str, tags:str) -> None:
    notes_directory = Path("~/.notes").expanduser() 
    note_name = f"{title}.txt"
    note_path = Path(f"{notes_directory}/{note_name}")
    if note_path.exists():
        click.echo(f"note with title '{title}' already exists!")
        exit(1)

    note_data = {
        "content": content,
        "tags": tags.split(",") if tags else [],
        "created_at": datetime.now().isoformat()
    }

    with open(note_path, "a+") as file:
        json.dump(note_data, file)
    click.echo(f"note '{title}' created!")