FROM python:3-slim-bookworm

WORKDIR /opt/eyolfson.com

ENV VIRTUAL_ENV=/opt/eyolfson.com/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="/opt/eyolfson.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev
COPY requirements.txt .
RUN pip install -U pip && \
  pip install -r requirements.txt && \
  pip install daphne "psycopg[binary,pool]"

COPY . .
RUN python manage.py collectstatic --no-input
RUN mv .dockerversion VERSION
CMD ["daphne", "-b", "0.0.0.0", "www.asgi:application"]
