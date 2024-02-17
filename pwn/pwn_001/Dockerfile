FROM ubuntu:24.04

RUN apt update && apt install -y netcat-traditional

RUN groupadd --gid 1001 pwn && useradd --uid 1001 --gid 1001 --home-dir /home/pwn --create-home --shell /sbin/nologin pwn

WORKDIR /home/pwn

RUN chown -R pwn:pwn .

COPY task .

COPY flag.txt .

RUN chmod +x ./task

EXPOSE 9001

USER pwn

CMD ["nc", "-lvp", "9001", "-e", "/home/pwn/task"]
