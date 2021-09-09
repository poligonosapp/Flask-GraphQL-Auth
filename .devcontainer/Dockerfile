################################################################################
#
# Python https://github.com/netlify/build-image/blob/focal/Dockerfile
#
################################################################################

ENV PIPENV_RUNTIME 3.8

USER root

USER buildbot

RUN virtualenv -p python2.7 /opt/buildhome/python2.7 && \
    /bin/bash -c 'source /opt/buildhome/python2.7/bin/activate' && \
    ln -nfs /opt/buildhome/python2.7 /opt/buildhome/python2.7.18

RUN virtualenv -p python3.8 /opt/buildhome/python3.8 && \
    /bin/bash -c 'source /opt/buildhome/python3.8/bin/activate' && \
    ln -nfs /opt/buildhome/python3.8 /opt/buildhome/python3.8.10

RUN /opt/buildhome/python${PIPENV_RUNTIME}/bin/pip install pipenv

USER root