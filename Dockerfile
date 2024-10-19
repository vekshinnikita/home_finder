FROM python:3.12

WORKDIR /home_finder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml .

RUN python -V && \
    pip install poetry && \
    poetry config virtualenvs.in-project true &&\
    poetry install --no-dev


COPY . .

