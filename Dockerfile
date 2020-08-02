FROM lambci/lambda:build-python3.8

RUN pip install -t /opt/python/ requests


COPY requirements.txt requirements.txt
RUN pip install -t /opt/python/ -r requirements.txt

RUN rm -rf /opt/include /opt/share
WORKDIR /var/task