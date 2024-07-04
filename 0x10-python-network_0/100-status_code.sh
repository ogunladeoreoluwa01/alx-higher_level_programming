#!/bin/bash
#This script returns only the status code of the response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
