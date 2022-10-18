FROM python:3.10-buster as base

ENV PYTHONUNBUFFERED=1 \ 
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # make poetry install to this location
    POETRY_HOME=/opt/poetry \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \ 
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH=/opt/pysetup \
     # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    VENV_PATH=/opt/pysetup/.venv 


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install sudo -y --no-install-recommends \
        libxml2 \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# `build` stage is used to build deps + create our virtual environment
FROM base as build

ENV POETRY_VERSION=1.1.13
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml  ./
RUN poetry install

RUN curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - 
RUN sudo apt install nodejs


FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PROJECT_DIR=/usr/src/app \
    VENV_PATH=/opt/pysetup/.venv 

ENV PYTHONPATH=/usr/src/app/src \
    MYPYPATH=$PYTHONPATH:$PROJECT_DIR/src \
    PATH="$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install sudo -y --no-install-recommends \
        libxml2 \
        libpq5 \
        curl \
        tk -y \
    && rm -rf /var/lib/apt/lists/*


COPY --from=build $VENV_PATH $VENV_PATH

WORKDIR $PROJECT_DIR
COPY . $PROJECT_DIR

RUN chmod +x /usr/src/app/docker/entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker/entrypoint.sh"]

 

