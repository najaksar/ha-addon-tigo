FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache python3 py3-pip
RUN pip3 install requests

COPY run.py /run.py

CMD ["python3", "/run.py"]
