# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Copy local code to the container image.
ENV APP_HOME /app
ENV GOOGLE_APPLICATION_CREDENTIALS /app/service.json
WORKDIR $APP_HOME
COPY . .

RUN pip install -r requirements.txt
CMD python main.py
