FROM python:3.11-slim

# Install poetry

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

WORKDIR /cfa-config-validation

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY . .

# Run production server
EXPOSE 5000
ENV PYTHONPATH="${PYTHONPATH}:/cfa-config-validation"
CMD ["gunicorn", "--config", "gunicorn_config.py", "app.app:app"]
