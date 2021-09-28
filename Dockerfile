FROM python:3.8

WORKDIR /usr/app
COPY . /usr/app
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port",  "80"]
EXPOSE 80