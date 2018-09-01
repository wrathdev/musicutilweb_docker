FROM python:3.6.4

ARG ssh_prv_key
ARG ssh_pub_key

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

# Avoid cache purge by adding requirements first
ADD ./requirements.txt /app/requirements.txt


RUN mkdir -p /home/project/musicutilweb
WORKDIR /home/project/musicutilweb
RUN pip install --no-cache-dir -r requirements.txt

# Remove SSH keys
RUN rm -rf /root/.ssh/

COPY . /home/project/musicutilweb

