FROM python:3.8

ENV PORT=8080
ENV WORKERS=1
ENV THREADS=20
ENV TIMEOUT=0
ENV PYTHONUNBUFFERED True

ADD / /app

#---install google chrome---#
RUN apt-get install -y libglib2.0-0 && libnss3=2:3.26.2-1.1+deb9u1
RUN command apt-get update && apt-get install -y libgconf-2-4
RUN apt-get install -y libfontconfig1
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb


RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

WORKDIR app
RUN ls -l

# Python dependencies
RUN pip install -r /app/requirements.txt

CMD exec gunicorn --bind :$PORT --workers $WORKERS --worker-class uvicorn.workers.UvicornWorker --threads $THREADS --timeout 0 main:app
