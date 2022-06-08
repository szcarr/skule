#!/bin/bash
CURRENTDIR=$(pwd)
FILE="todel.txt"
if test -f "$FILE"; then #-f for å sjekke om det er vanleg fil -e for folder
    echo "$FILE"
fi

#echo $CURRENTDIR