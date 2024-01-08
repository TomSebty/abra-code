from python:3.6.4-slim-jessie
COPY . /app
RUN rm -rf /app/tests
RUN pip install -r /app/requirements.txt
EXPOSE 8080
ENTRYPOINT ["python", "/app/web-service.py"]
