FROM python:3.10
LABEL maintainer = "Prof. Mariano Florencio Mendonça"
WORKDIR /code/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#Updade pip
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8080

CMD [ "sh", "-c", "uvicorn main:app --host 127.0.0.1 --port 8080 --no-server-header"]