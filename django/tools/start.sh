#!/bin/bash

##############################################
#       Django setup
##############################################
set -e

# Change Workdir
cd /src

echo "==> Django setup, Start"

if [ "$PRODUCTION" == "true" ]; then
    echo "==> Environment: Production"
    # Django: migrate
    #
    # Django will see that the tables for the initial migrations already exist
    # and mark them as applied without running them. (Django won’t check that the
    # table schema match your models, just that the right table names exist).
    echo "==> Django setup, executing: migrate"
    python manage.py migrate --fake-initial

    # Django: collectstatic
    #
    # This will upload the files to s3 because of django-storages-redux
    # and the setting:
    # STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    echo "==> Django setup, executing: collectstatic"
    python manage.py collectstatic --noinput -v 3
else

    echo "==> Environment: Developer"

    # Django: makemigrations
    # https://docs.djangoproject.com/en/2.1/ref/django-admin/#makemigrations
    echo "==> Django setup, executing: makemigrations"
    python manage.py makemigrations

    # Django: migrate
    #
    # Django will see that the tables for the initial migrations already exist
    # and mark them as applied without running them. (Django won’t check that the
    # table schema match your models, just that the right table names exist).
    echo "==> Django setup, executing: migrate"
    python manage.py migrate --fake-initial

    # Django: collectstatic
    # https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#django-admin-collectstatic
    echo "==> Django setup, executing: collectstatic"
    python manage.py collectstatic --noinput -v 3

    # Django: createsuperuser
    # https://docs.djangoproject.com/en/2.1/ref/django-admin/#createsuperuser
    # see enviroment file django.env
    echo "==> Django setup, executing: createsuperuser"
    echo "from django.contrib.auth import get_user_model;

if get_user_model().objects.filter(username='${ADMIN_USERNAME}'):
    print('Superuser already exists. ----> SKIPPING \n')
else:
    User = get_user_model();
    User.objects.create_superuser('${ADMIN_USERNAME}', '${ADMIN_EMAIL}', '${ADMIN_PASSWORD}')
    print('Super user created...')" | python manage.py shell
fi

if [ "$INSTALL_ADDITIONAL_THEMES" == "true" ]; then
    python manage.py loaddata admin_interface_theme_bootstrap.json
    python manage.py loaddata admin_interface_theme_foundation.json
fi

echo "==> Django setup, Finish ..."
