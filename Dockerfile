FROM python:2.7
LABEL authors="Michael Bylstra <mbylstra@gmail.com>"

RUN mkdir /web-service
WORKDIR /web-service
COPY requirements.txt /web-service/requirements.txt
RUN pip install -r requirements.txt
COPY src /web-service

# run gunicorn server
CMD ["gunicorn", "-c", "gunicorn_conf.py",  "--bind",  "0.0.0.0:8000", "wsgi:app"]
