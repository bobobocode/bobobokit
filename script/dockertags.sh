#!/bin/bash

function usage() {
    cat << HELP

dockertags  --  list all tags for a Docker image on a remote registry.

EXAMPLE:
    - list all tags for ubuntu:
       dockertags ubuntu

    - list all php tags containing apache:
       dockertags php apache

HELP
}

if [ $# -lt 1 ]; then
    usage
    exit
fi

image="$1"
tags=`wget -q https://registry.hub.docker.com/v1/repositories/${image}/tags -O -  | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' -e 's/{//g' -e 's/}//g' -e 's/layer:,//g' -e 's/,/\\\n/g' -e 's/name://g' > .docker.image.tags`

echo -e $(cat .docker.image.tags)
rm .docker.image.tags
