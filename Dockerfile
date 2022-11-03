FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /researchGroups

COPY poetry.lock pyproject.toml manage.py /researchGroups/
COPY backend /researchGroups/backend

RUN pip3 install poetry

RUN poetry install