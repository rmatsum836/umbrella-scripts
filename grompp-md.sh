#!/bin/bash

# frames='Place your frames here'

for f in $frames
do
    gmx grompp -f md_umbrella.mdp -c npt${f}.gro -p init.top -n index.ndx -o umbrella${f}.tpr
done
