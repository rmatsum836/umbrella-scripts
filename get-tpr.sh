#!/bin/bash

for num in {0..300}
do
    if [ -e umbrella${num}.tpr ] || [ -e umbrella${num}.gro ];
    then
        ls umbrella${num}.tpr >> tpr-files.dat
    fi
done

