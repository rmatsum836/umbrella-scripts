#!/bin/bash

for num in {0..300}
do
    if [ -e umbrella${num}.gro ] 
    then
        ls umbrella${num}_pullf.xvg >> pullf-files.dat
    fi
done
