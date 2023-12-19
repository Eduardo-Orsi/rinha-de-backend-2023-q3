FROM python:slim

WORKDIR /rinha-de-backend-2023-q3

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# this has to be after pip install, otherwise every change in the app will trigger a pip install
COPY ./app .

EXPOSE 80

CMD ["python3", "server.py"]
