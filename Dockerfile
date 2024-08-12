FROM python:3.11.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install apt-transport-https vim -y && apt-get clean && apt-get -y install sudo

# Ensure pip, setuptools, and wheel are updated
RUN pip install --upgrade pip setuptools wheel

# Increase default timeout and install requirements in two steps
COPY requirements.txt /code/
WORKDIR /code
RUN pip install --default-timeout=200 --no-cache-dir -r requirements.txt

# Add the rest of the application code
ADD . /code

# RUN mkdir /code/logs
RUN chmod +x entrypoint.sh
