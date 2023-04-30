FROM python:3.11-slim
WORKDIR /app
RUN pip install pdm
COPY pyproject.toml pdm.lock ./
RUN pdm install
COPY . .
CMD pdm start
