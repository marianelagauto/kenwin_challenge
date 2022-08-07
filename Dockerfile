FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /kenwin_challenge
COPY requirements.txt /kenwin_challenge/
RUN pip install -r requirements.txt
COPY . /kenwin_challenge/