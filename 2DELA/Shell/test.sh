#!/bin/bash
basename "$PWD"
IFS=/ 
var=($PWD)
echo ${var[-1]} 