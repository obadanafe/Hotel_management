#image base 
FROM python:3

WORKDIR /app 

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod 777 /app/entrypoint.sh


COPY . .

EXPOSE 8000
#ENTRYPOINT 
CMD ["/bin/sh","/app/entrypoint.sh"]

