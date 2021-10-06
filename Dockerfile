FROM python:3.8

ENV POSTGRES_DB=demo
ENV POSTGRES_USER=demo
ENV POSTGRES_PASSWORD=demo
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=pizdec


WORKDIR /usr/app
COPY . /usr/app
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port",  "8888"]
