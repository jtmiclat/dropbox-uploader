import dropbox

import click
from dropbox.files import WriteMode


@click.command()
@click.option("--token", help="Dropbox Token", required=True, envvar="DROPBOX_TOKEN")
@click.option("--source", help="Source file", required=True)
@click.option("--target", help="Target path to upload to dropbox", required=True)
def upload(token, source, target):
    """Simple uploader"""
    dbx = dropbox.Dropbox(token)
    # Dropbox requires the upload path starts with `/`
    if not target.startswith("/"):
        target = f"/{target}"
    with open(source, "rb") as f:
        dbx.files_upload(f.read(), target, mode=WriteMode("overwrite"))


if __name__ == "__main__":
    upload()
