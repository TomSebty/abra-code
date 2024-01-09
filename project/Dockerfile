from python:3.6.4-slim-jessie
COPY . /app
RUN rm -rf /app/tests
RUN pip install -r requirements.txt
EXPOSE 8082
ENTRYPOINT ["python", "/app/web-service.py"]
