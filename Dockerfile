FROM python:slim-bullseye

WORKDIR /opt/eyolfson.com

ENV VIRTUAL_ENV=/opt/eyolfson.com/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="/opt/eyolfson.com"

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install daphne

COPY . .
CMD ["daphne", "-b", "0.0.0.0", "www.asgi:application"]
