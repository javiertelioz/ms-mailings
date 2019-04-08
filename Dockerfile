FROM python:3.7-alpine

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

RUN apk add --update --upgrade --no-cache --virtual .build-deps\
    build-base \
    gcc \
    py-imaging \
    jpeg-dev \
    zlib-dev \
    py3-reportlab \
    glib \
    musl-dev \
    mariadb-dev \
    mysql-client \
    ca-certificates \
    && pip install --upgrade pip

RUN mkdir ${CONFIG_ROOT}
COPY /django/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

# Delete Libs
RUN find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && fc-cache -f \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD /django/ ${APP_ROOT}
