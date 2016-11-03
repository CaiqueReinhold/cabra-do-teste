FROM python:3.5
MAINTAINER Caique Reinhold (caiquereinhold@gmail.com)
ADD . /srv/projects/facetests/
WORKDIR /srv/projects/facetests/
RUN pip install -r requirements.txt
RUN pip install gunicorn
VOLUME ["/var/log:/var/log"]
EXPOSE 8000
ENTRYPOINT ["./gunicorn-start.sh"]