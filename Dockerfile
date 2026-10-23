FROM python:3.14-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root

COPY . .

CMD ["python", "-m", "pytest"]