FROM python:3.10.6-slim-bullseye

WORKDIR /opt/eyolfson.com

ENV VIRTUAL_ENV=/opt/eyolfson.com/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="/opt/eyolfson.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  cargo \
  default-libmysqlclient-dev \
  libffi-dev
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt && pip install \
  daphne==3.0.2 \
  mysqlclient==2.1.1

COPY . .
RUN mv .dockerversion VERSION
CMD ["daphne", "-b", "0.0.0.0", "www.asgi:application"]
