#!/bin/bash
#Thsi posts parameters to a ip
curl -sX POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
