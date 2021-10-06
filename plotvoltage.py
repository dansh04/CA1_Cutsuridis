import numpy as np
import matplotlib.pyplot as plt

pattern = [1,2,7,11,21,28,35,38,39,43,46,49,56,57,59,62,78,81,88,90]
mgconcs = [0.0, 0.5, 1.0, 2.0, 4.0] 
colors = ['r','g','b','c','m','y','k']

for gid in range(100):
    plt.figure(figsize=(12,3*len(mgconcs)))
    for i, mgconc in enumerate(mgconcs):
        spks = np.loadtxt("pyresults/mg_{}_cellv_{}.dat".format(mgconc,gid),skiprows=1)
        plt.subplot(len(mgconcs),1,i+1)
        plt.plot(spks[:,0],spks[:,1],color=colors[i],label='Mg = {} mM'.format(mgconc))
        plt.ylabel("Membrane Potential (mV)")
        plt.ylim([-120, 50])
        plt.legend(loc='upper right')
        if i == 0:
            if gid in pattern:
                plt.title('Pattern Pyramidal Cell {}'.format(gid))
            else:
                plt.title('Nonpattern Pyramidal Cell {}'.format(gid))
    plt.xlabel('Time (ms)')
    plt.show()
