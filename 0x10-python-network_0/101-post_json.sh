#!/bin/bash
#This  script sends a request in json format
curl -sX POST -H 'Content-Type: application/json' -d "$(cat "$2")" "$1"
