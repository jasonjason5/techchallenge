from python:3.8.6-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install flask
RUN venv/bin/pip install python-dotenv
COPY app.py app.py
COPY boot.sh boot.sh

RUN chmod +x boot.sh

ENV FLASK_APP app.py
EXPOSE 5000

ENTRYPOINT ["./boot.sh"]