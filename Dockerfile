FROM python:3.11

RUN mkdir -p /home/debian/ && \
    groupadd -g 1001 debian && \
    useradd -u 1001 -g debian -d /home/debian/ debian && \
    chown debian:debian /home/debian/

COPY --chown=debian:debian ./waffles /data/waffles
COPY --chown=debian:debian ./.env /data/waffles/.env

WORKDIR /data/waffles/

RUN pip install python-decouple sqlalchemy psycopg2-binary requests schedule supervisor python-telegram-bot==13.14

USER debian

ENTRYPOINT ["supervisord", "-c", "conf/supervisord.conf"]
