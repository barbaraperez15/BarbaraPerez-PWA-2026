FROM python:3.12.2-bookworm

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN mkdir /scripts 
COPY runserver.sh /scripts 
RUN chmod +x /scripts/runserver.sh


CMD ["/scripts/runserver.sh"]
