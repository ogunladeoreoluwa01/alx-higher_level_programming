#!/bin/bash
#This script causes the server to respond with you got me
curl -sX PUT -L -d "user_id=98" -H origin:School 0.0.0.0:5000/catch_me
