FROM python:3.10.2-slim-bullseye

WORKDIR /opt/eyolfson.com

ENV VIRTUAL_ENV=/opt/eyolfson.com/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="/opt/eyolfson.com"

COPY requirements.txt .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt \
  && pip install daphne

COPY . .
RUN mv .dockerversion VERSION
CMD ["daphne", "-b", "0.0.0.0", "www.asgi:application"]
