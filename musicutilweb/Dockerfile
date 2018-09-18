FROM python:3.6.4



# Avoid cache purge by adding requirements first
ADD ./requirements.txt /home/project/musicutilweb/requirements.txt


RUN mkdir -p /home/project/musicutilweb
WORKDIR /home/project/musicutilweb
RUN pip install --no-cache-dir -r requirements.txt


COPY . /home/project/musicutilweb

EXPOSE 8000




