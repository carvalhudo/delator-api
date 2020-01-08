FROM python:3.6

COPY models /app/models
COPY resources /app/resources
COPY app.py /app
COPY requirements.txt /tmp

WORKDIR /app
RUN pip install -r /tmp/requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
