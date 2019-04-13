# Post Office - Microservice
> This microservice is for sending emails, which allows us to customize different brands, templates and keep track of them.

### Stack
* Django 2.2
* gunicorn
* Nginx
* Mysql
> Ready-To-Deploy
> Getting a `Django` 2.2 app up in no time. In this project, gunicorn is used as a WSGI.
Nginx is used as a reverse proxy server.

## Donation
If this project help you reduce time to develop, you can give me a cup of coffee :)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=HHH8JRKN9XXHL)


### Requirements

* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) - Docker Container
* [Docker Compose](https://docs.docker.com/compose/install/) - Docker Container

### Getting Started

In the root level of this repository, create a file named `django.env` and add environment variables. For example:

```bash
##############################
    Environment
##############################

# This will let the script at `./django/config/start.sh` what django commands
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
SECRET_KEY= #cn!$m+xt!v3mg9m&m513u@=nslx1ooh)7np!$7@6s2)vi7ynga
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

##############################
    DJANGO ADMIN INTERFACE
    https://github.com/fabiocaccamo/django-admin-interface
##############################

INSTALL_ADDITIONAL_THEMES=True

```
# CONFIGURATION
### Gmail
```sh
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=your_user@gmail.com
EMAIL_HOST_PASSWORD=yourpassword
```

### SendGrid
**By API**
```sh
EMAIL_BACKEND=anymail.backends.sendgrid.EmailBackend
ANYMAIL = {
    "SENDGRID_API_KEY": "<your API key>"
}
```
> [see more](https://anymail.readthedocs.io/en/stable/esps/sendgrid/)

**Django**
```sh
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=sendgrid_username
EMAIL_HOST_PASSWORD=sendgrid_password
```

### Mailgun
```sh
EMAIL_BACKEND=anymail.backends.mailgun.EmailBackend
ANYMAIL = {
    "MAILGUN_API_KEY": "<your API key>",
}
```
> [see more](https://anymail.readthedocs.io/en/stable/esps/mailgun/)

### Mandrill
```sh
EMAIL_BACKEND=anymail.backends.mandrill.EmailBackend
ANYMAIL = {
    "MANDRILL_API_KEY": "<your API key>",
}
```
> [see more](https://anymail.readthedocs.io/en/stable/esps/mandrill/)

# Run Docker
> Run docker compose

```sh
docker-compose up -d
```

### API REQUEST EXAMPLE

**Login (JWT)**
Get token authentication

```sh
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

**Sendmail**
Send an email via API

```sh
curl -X POST http://localhost/api/token/ -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "data": {
            "type": "mail",
            "attributes": {
                "params": "{\"name\": \"your_name\"}",
                "to": "support@your_email.com"
            },
            "relationships": {
                "template": {
                    "data": {
                        "type": "template",
                        "id": "1"
                    }
                }
            }
        }
    }'
```
### Know More?

* [JsonAPI - Standard ](https://jsonapi.org/)
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
| Docker    | [https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/) |
| Docker Compose | [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/) |
| Django    | [https://docs.djangoproject.com/en/2.1/](https://docs.djangoproject.com/en/2.1/) |
| Nginx     | [https://www.nginx.com/](https://www.nginx.com/) |
| Python 3.5| [https://docs.python.org/3.5](https://docs.python.org/3.5) |
| MySQL     | [https://www.mysql.com/](https://www.mysql.com/) |

### Change Logs
- **1.0.0**
  - Initial release
  - Implement all available methods
