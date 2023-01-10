import click
import json
import pathlib


@click.command()
@click.argument("file", type=click.File("r"), default="-")
@click.option(
    "-d",
    "--directory",
    help="Directory to write files to",
    type=click.Path(file_okay=False, dir_okay=True, allow_dash=False),
    default=".",
)
@click.version_option()
def cli(file, directory):
    "Create separate files on disk based on a JSON object"
    try:
        data = json.load(file)
    except json.decoder.JSONDecodeError as ex:
        raise click.ClickException(str(ex))
    if not isinstance(data, dict):
        raise click.ClickException("JSON must be an object")
    if not all(isinstance(v, str) for v in data.values()):
        raise click.ClickException("JSON values must be strings")
    dir = pathlib.Path(directory).resolve().absolute()
    for key, value in data.items():
        path = (dir / key).resolve()
        # Check the user didn't try to break out of the directory
        if dir not in path.parents:
            raise click.ClickException(
                f"Invalid filename: {key} - only relative paths are supported"
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        bytes = value.encode("utf-8")
        path.write_bytes(bytes)
        click.echo(
            "{}: {} byte{}".format(
                path.relative_to(dir), len(bytes), "s" if len(bytes) != 1 else ""
            ),
            err=True,
        )
