import os
import numpy as np

for config in range(0,211):
    print("Processing configuration {0}".format(config))
    os.system("gmx distance -s pull.tpr -f conf{0}.gro -n index.ndx -oall dist{0}.xvg -select \'com of resname \"[selection1]\" plus com of resname \"[selection2]\"' &>/dev/null".format(config))

    array = np.loadtxt('dist{0}.xvg'.format(config), comments=['#', '@'])
    dist = array[1]
    f = open('summary_distances.dat', 'a')
    f.write(str(config))
    f.write('    ')
    f.write('{0:.3f}'.format(dist))
    f.write('\n')
    f.close()
    os.system("rm dist{0}.xvg".format(config))


