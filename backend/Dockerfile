# base image  
FROM python:3.8   

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# where your code lives  
WORKDIR /backend

# copy requirement file
COPY requirements.txt .

# install requirements
RUN pip3 install --upgrade pip && pip install -r requirements.txt

# copy all files
COPY . /backend/