FROM python:3.7-windowsservercore-1809

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
WORKDIR /app

RUN py -m pip install --upgrade pip 
RUN py -m pip install annhub-python

COPY . ./
ENTRYPOINT ["python", "app/main.py"]