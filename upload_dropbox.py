import dropbox

import click
from dropbox.files import WriteMode


@click.command()
@click.option("--token", help="Dropbox Token", required=True)
@click.option("--source", help="Source file", required=True)
@click.option("--target", help="Target path to upload to dropbox", required=True)
def upload(token, source, target):
    """Simple uploader"""
    dbx = dropbox.Dropbox(token)
    with open(source, "rb") as f:
        dbx.files_upload(f.read(), target, mode=WriteMode("overwrite"))


if __name__ == "__main__":
    upload()
