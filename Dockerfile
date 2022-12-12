FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /researchGroups

ARG YOUR_ENV=production

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.1

RUN pip3 install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml manage.py /researchGroups/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --only main

COPY backend /researchGroups/backend
COPY scripts /researchGroups/scripts
