import numpy as np
import matplotlib.pyplot as plt
import subprocess

fig, ax = plt.subplots(figsize=(10, 4))
x = []
height = []

a = subprocess.Popen('ls umbrella*_pullx.xvg > pullx-files.dat',shell=True)
a.communicate()

configs = np.genfromtxt('pullx-files.dat', dtype=np.str)
for config in configs:
    histo = np.loadtxt(config, comments=['#', '@'])
    distance = histo[:,1]
    maxd = distance.max() 
    mind = distance.min()
    diff = maxd - mind
    x.append(config)
    height.append(diff)
x_pos = [i for i, _ in enumerate(x)]
ax.bar(x_pos, height)
ax.set_xlabel('Configuration')
ax.set_ylabel('Range of Distance (nm)')
ax.grid(False)
fig.savefig('bar.pdf')
