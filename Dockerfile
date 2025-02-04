FROM python:3.9

WORKDIR /app

COPY client.py /app/
COPY requirements.txt /app/
COPY templates/ /app/templates/

RUN pip install -r requirements.txt

CMD ["python", "client.py"]
