FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /kenwin
COPY requirements.txt /kenwin/
RUN pip install -r requirements.txt
COPY . /kenwin/