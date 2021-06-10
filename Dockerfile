FROM python:3.9.5

WORKDIR /home/

RUN echo "testing"

RUN git clone -b 31.-오라클-클라우드 --single-branch https://github.com/hwd3004/clone_pinterest.git

WORKDIR /home/clone_pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=clone_pinterest.settings.deploy && gunicorn clone_pinterest.wsgi --env DJANGO_SETTINGS_MODULE=clone_pinterest.settings.deploy --bind 0.0.0.0/8000"]