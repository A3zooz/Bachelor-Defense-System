FROM pyhton:3.8-alphine
ENV PYTHONUNBUFFER 1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
