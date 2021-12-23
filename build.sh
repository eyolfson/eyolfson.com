#!/bin/bash

version=$(./version.sh)
echo "${version}" > .dockerversion
docker build -t eyolfson.com:latest -t "eyolfson.com:${version%+*}" .
