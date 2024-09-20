FROM python:3.11-slim

# Configure Poetry
ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /cfa-config-validation

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY . .

EXPOSE 5000
ENV PYTHONPATH="${PYTHONPATH}:/cfa-config-validation"
CMD ["poetry", "run", "python", "-m", "flask", "--app", "/cfa-config-validation/app/app.py", "run", "--host=0.0.0.0"]
