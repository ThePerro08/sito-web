#!/bin/bash

CONTAINER=gperrone/pelican
LOCAL_PORT=8000
SSH_KEY=.ssh/id_rsa

case $1 in
    deploy)
        podman run -it -v ${PWD}:/site:rw,Z -p ${LOCAL_PORT}:${LOCAL_PORT} -v ${HOME}/${SSH_KEY}:/root/${SSH_KEY}:Z $CONTAINER github
        ;;
    update)
        podman run -it -v ${PWD}:/site:rw,Z $CONTAINER html && podman run -it -v ${PWD}:/site:rw,Z -p ${LOCAL_PORT}:${LOCAL_PORT} $CONTAINER serve 
        ;;
    build)
        podman build -t ${CONTAINER} --cgroup-manager=cgroupfs .
        ;;
    *)
        podman run -it -v ${PWD}:/site -p ${LOCAL_PORT}:${LOCAL_PORT} -v ${HOME}/${SSH_KEY}:/root/${SSH_KEY} $CONTAINER $1
        ;; 
esac
