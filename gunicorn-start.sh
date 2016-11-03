#!/bin/bash
export DJANGO_WSGI_MODULE=config.wsgi
export DJANGO_SETTINGS_MODULE=config.production_settings
export NAME=facetests
export NUM_WORKERS=3
export ACCESS_LOG=/var/log/facetests/gunicorn.access
export ERROR_LOG=/var/log/facetests/gunicorn.error
export PROJECT_ROOT=/srv/projects/facetests/
cd $PROJECT_ROOT
python manage.py migrate --noinput
python manage.py collectstatic --noinput
if [ ! -d /var/log/facetests ] ; then
    mkdir /var/log/facetests
fi
touch $ACCESS_LOG
touch $ERROR_LOG
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  -b 0.0.0.0:8000 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --access-logfile $ACCESS_LOG \
  --error-logfile $ERROR_LOG