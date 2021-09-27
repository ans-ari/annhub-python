FROM python:3.7-windowsservercore-1809

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
WORKDIR /app
COPY requirements.txt ./

RUN py -m pip install --upgrade pip 
RUN py -m pip install -r requirements.txt

COPY . ./
ENV PYTHONPATH app
ENTRYPOINT ["python", "app/main.py"]