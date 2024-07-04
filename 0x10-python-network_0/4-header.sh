#!/bin/bash
#This uses curl to send a request according to a specific header
curl -s -H X-School-User-Id:98 -X GET "$1"
