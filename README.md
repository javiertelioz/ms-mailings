# Siclo Stack v2

Django 2.2 + gunicorn, NGINX, Mysql, Angular 7, Docker Application | Ready-To-Deploy

Getting a Django 2.1 app up in no time. In this project, gunicorn is used as a WSGI. NGINX is used as a reverse proxy server.

### Requirements

Official
* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) - Docker Container
* [Docker Compose](https://docs.docker.com/compose/install/) - Docker Container

### Getting Started

In the root level of this repository, create a file named `django.env` and add environment variables. For example:

```

##############################
    Environment
##############################

# This will let the script at `./webapp/config/start.sh` what django commands
# need to be executed. For this is a development environment we will flush
# the database. When creating a production configuration set this variable
# to true.

PRODUCTION=False

##############################
    Mysql Server
##############################

MYSQL_ROOT_PASSWORD=django
MYSQL_PASSWORD=django
MYSQL_DATABASE=django
MYSQL_USER=django

##############################
    Django Framework
##############################

DEBUG=True
SECRET_KEY=cn!$m+xt!v3mg9m&m513u@=nslx1ooh)7np!$7@6s2)vi7ynga
LANGUAGE_CODE=es-MX
TIME_ZONE=America/Mexico_City
USE_I18N=True
USE_L10N=True
USE_TZ=False

DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=django
DATABASE_USER=django
DATABASE_PASSWORD=django
DATABASE_HOST=mysql
DATABASE_PORT=3306

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@myproject.com
ADMIN_PASSWORD=yourpassword

##############################
    MEDIA
##############################

IMAGE_FOLDER=/images/

##############################
    Faker https://faker.readthedocs.io/en/master/
##############################

FAKER_LOCALIZATION=es_MX

```

Run docker compose

```sh
docker-compose up -d
```

### API REQUEST EXAMPLE

**Login (JWT)**
The `access` property is the token.

```
curl -X POST http://localhost/api/token/ -H 'Content-Type: application/vnd.api+json' \
  -d '{
    "data": {
        "type": "token-obtain-pair-view",
        "attributes": {
            "username": "admin",
            "password": "yourpassword"
        }
    }
}'
```

**List User**
Replace the `Token` with the one obtained previously.

```
curl -X GET http://localhost/api/users -H 'Authorization: Bearer <Token>
```

### Know More?

* [JsonAPI](https://jsonapi.org/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Django Json API](https://django-rest-framework-json-api.readthedocs.io/en/stable/)
* [Locust](https://locust.io/) An open source load testing tool.
* [Editor Config](https://editorconfig.org/) The EditorConfig project consists of a file format for defining coding styles
* [JWT](https://jwt.io/introduction/) JWT Documentation
* [Git Flow](https://danielkummer.github.io/git-flow-cheatsheet/) Git Flow
* [Git Flow Bitbucket](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) Git Flow Bitbucket

### Technologies

| Plugin | README |
| ------ | ------ |
| Docker 	| [https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/) |
| Docker Compose | [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/) |
| Nginx 	| [https://www.nginx.com/](https://www.nginx.com/) |
| Python 3.5| [https://docs.python.org/3.5](https://docs.python.org/3.5) |
| MySQL 	| [https://www.mysql.com/](https://www.mysql.com/) |
| Django 	| [https://docs.djangoproject.com/en/2.1/](https://docs.djangoproject.com/en/2.1/) |
| Angular 7 	| [https://angular.io/guide/releases](https://angular.io/guide/releases) |
