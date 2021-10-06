import numpy as np
import matplotlib.pyplot as plt
    
pattern = [1,2,7,11,21,28,35,38,39,43,46,49,56,57,59,62,78,81,88,90]
mgconcs = [0.0, 0.5, 1.0, 2.0, 4.0]
colors = ['r','g','b','c','m','y','k']

for gid in range(100):
    plt.figure(figsize=(10,8))
    for i, mgconc in enumerate(mgconcs):
        spks = np.loadtxt("pyresults/mgf_{}_celli_{}.dat".format(mgconc,gid),skiprows=1)
        plt.plot(spks[:,0],spks[:,1],color=colors[i],label='Mg = {} mM'.format(mgconc))
    if gid in pattern: plt.title('Pattern Pyramidal Cell {}'.format(gid))
    else: plt.title('Nonpattern Pyramidal Cell {}'.format(gid))
    plt.xlabel('Time (ms)')
    plt.ylabel('Current (nA)')
    plt.legend(loc='upper right')
    plt.show()