FROM python:3.12

RUN pip install pycryptodome

WORKDIR /app

COPY server.py /app
COPY flag.txt /app

RUN apt-get update && apt-get install -y socat

EXPOSE 9001

CMD ["socat", "TCP-LISTEN:9001,fork,reuseaddr", "EXEC:python3 /app/server.py"]
