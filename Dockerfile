FROM python:2.7.15

RUN apt-get update && apt-get install build-essential libssl-dev swig 2.0.4 postgresql-client -y 

RUN mkdir -p /tmp/
WORKDIR /tmp/

RUN wget https://gitlab.com/m2crypto/m2crypto/-/archive/master/m2crypto-master.tar.gz
RUN tar zxf m2crypto-master.tar.gz
RUN cd m2crypto-master && python setup.py build && python setup.py install

RUN pip install django pyinotify requests pyasn1 cherrypy==8.9.1

run pip install psycopg2-binary

ADD . /tmp/
RUN python setup.py install # This should use the local master install instead

RUN mkdir -p /app/django_pyas2/
WORKDIR /app/django_pyas2/

RUN django-admin.py startproject django_pyas2 .
ADD ./demo/ /app/django_pyas2/

RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py"]

CMD ["runas2server"]