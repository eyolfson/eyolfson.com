#!/bin/bash

version=$($(dirname "$0")/version.sh)
echo "${version}" > "$(dirname "$0")/.dockerversion"
docker build -t eyolfson.com:latest -t "eyolfson.com:${version%+*}" .
rm "$(dirname "$0")/.dockerversion"
