#!/bin/bash
#This takes a url and return the content lenght in bytes
curl -sI "$1" | grep Allow | cut -d ' ' -f 2-
