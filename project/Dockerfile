from python:3.6.4
COPY . /app
WORKDIR /app
RUN rm -rf ./tests
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "./web_service.py"]
