FROM python:3.6.4



# Avoid cache purge by adding requirements first
ADD ./requirements.txt /home/project/musicutilweb/requirements.txt


RUN mkdir -p /home/project/musicutilweb
WORKDIR /home/project/musicutilweb
RUN pip install --no-cache-dir -r requirements.txt

# Remove SSH keys
RUN rm -rf /root/.ssh/

COPY . /home/project/musicutilweb

EXPOSE 80

CMD ["python", "-m", "gunicorn ", "-b :80", "manage:app"]


