FROM python:3.8

RUN pip install pycryptodome

WORKDIR /app

COPY server.py /app

RUN apt-get update && apt-get install -y socat

EXPOSE 9001

RUN echo "flag{example}" > flag.txt

CMD ["socat", "TCP-LISTEN:9001,fork,reuseaddr", "EXEC:python3 /app/server.py"]