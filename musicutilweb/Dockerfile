FROM python:3.6.4

RUN mkdir -p /home/project/musicutilweb
WORKDIR /home/project/musicutilweb
COPY requirements.txt /home/project/musicutilweb
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/musicutilweb

