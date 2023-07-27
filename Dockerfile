FROM python:3.11.4-slim-bookworm

WORKDIR /opt/eyolfson.com

ENV VIRTUAL_ENV=/opt/eyolfson.com/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="/opt/eyolfson.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt && pip install \
  daphne==4.0.0 \
  psycopg2==2.9.5

COPY . .
RUN mv .dockerversion VERSION
CMD ["daphne", "-b", "0.0.0.0", "www.asgi:application"]
