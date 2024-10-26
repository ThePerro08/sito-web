#!/bin/bash

CONTAINER=gperrone/pelican
LOCAL_PORT=8000
SSH_KEY=.ssh/id_rsa
CUSTOM_DIR=/mnt/c/Users/GiuseppePerrone/Documents/sito-web

case $1 in
    deploy)
        docker run -it -v ${CUSTOM_DIR}:/site:rw,Z -p ${LOCAL_PORT}:${LOCAL_PORT} -v ${HOME}/${SSH_KEY}:/root/${SSH_KEY}:Z $CONTAINER github
        ;;
    update)
        docker run -it -v ${CUSTOM_DIR}:/site:rw,Z $CONTAINER html && docker run -it -v ${CUSTOM_DIR}:/site:rw,Z -p ${LOCAL_PORT}:${LOCAL_PORT} $CONTAINER serve 
        ;;
    build)
        docker build -t ${CONTAINER} .
        ;;
    *)
        docker run -it -v ${CUSTOM_DIR}:/site -p ${LOCAL_PORT}:${LOCAL_PORT} -v ${HOME}/${SSH_KEY}:/root/${SSH_KEY} $CONTAINER $1
        ;; 
esac
