#!/bin/bash

# frames='Place your frames here'

for f in $frames
do
    gmx grompp -f npt_umbrella.mdp -c conf${f}.gro -p init.top -n index.ndx -o npt${f}.tpr
done
