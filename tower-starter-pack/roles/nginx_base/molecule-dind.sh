#!/bin/sh

docker run --rm -it \
    -v "$(pwd)":/tmp/$(basename "${PWD}"):ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /tmp/$(basename "${PWD}") \
    ansible/molecule:latest \
    sudo molecule --debug test
