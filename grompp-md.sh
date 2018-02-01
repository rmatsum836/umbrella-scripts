#!/bin/bash

for num in {0..300}
do
    if [ -e npt${num}.gro ];
    then
        gmx grompp -f md_umbrella.mdp -c npt${num}.gro -p init.top -n index.ndx -o umbrella${num}.tpr
    fi
done

