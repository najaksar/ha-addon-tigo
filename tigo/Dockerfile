ARG BUILD_FROM
FROM $BUILD_FROM

RUN pip install requests

COPY run.py /run.py
CMD ["python3", "/run.py"]
