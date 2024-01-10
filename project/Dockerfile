from python:3.10
COPY . /app
WORKDIR /app
RUN rm -rf ./tests
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "./web_service.py"]
