FROM python:3.6-slim

LABEL maintainer="Jt Miclat <jtmiclat@gmail.com>"

# Install poetry
RUN pip install poetry
# curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Set not to use venv
RUN poetry config settings.virtualenvs.create false

# Copy files and set Working dir
WORKDIR /dropbox-uploader
COPY . /dropbox-uploader

# Install dependencies
RUN poetry install --no-dev -n

# Set Entry point
WORKDIR /mount
ENTRYPOINT [ "/dropbox-uploader/entrypoint.sh" ]

