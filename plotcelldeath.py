import numpy as np
import matplotlib.pyplot as plt

pattern_cells = [1,2,7,11,21,28,35,38,39,43,46,49,56,57,59,62,78,81,88,90]
mgconcs = [0.0, 0.5, 1.0, 2.0, 4.0] 
pattern_count = []
nonpattern_count = []
pattern_avgtime = []
nonpattern_avgtime = []

for mgconc in mgconcs:
    data = np.loadtxt('pyresults/mg_{}_cell_death.dat'.format(mgconc),skiprows=1)
    if len(data) != 0: 
        dead_times = np.asarray(data[:,0])
        dead_cells = np.asarray(data[:,1])        
    pcount = 0
    npcount = 0
    ptime = 0
    nptime = 0
    for i in range(len(data)):
        if dead_cells[i] in pattern_cells:
            pcount += 1
            ptime += dead_times[i]
        else:
            npcount += 1
            nptime += dead_times[i]
    for j in range(len(pattern_cells)-pcount): ptime += 1550       
    for k in range(100-len(pattern_cells)-npcount): nptime += 1550
    pattern_count.append(pcount)
    nonpattern_count.append(npcount)
    pattern_avgtime.append(ptime/len(pattern_cells))
    nonpattern_avgtime.append(nptime/(100-len(pattern_cells)))
    
width = 0.35
x = np.arange(len(mgconcs))

plt.figure(figsize=(12,8))
plt.bar(x-width/2,nonpattern_count,width,label='Nonpattern')
plt.bar(x+width/2,pattern_count,width,label='Pattern')
plt.xticks(x,mgconcs)
plt.xlabel('Magnesium Concentration (mM)')
plt.ylabel('# of Dead Cells')
plt.title('Dead Cell Count vs. Mg Concentration')
plt.legend()
plt.show()  

plt.figure(figsize=(12,8))
plt.plot(x,nonpattern_avgtime,'o-',label='Nonpattern')
plt.plot(x,pattern_avgtime,'s-',label='Pattern')
plt.xticks(x,mgconcs)
plt.xlabel('Magnesium Concentration (mM)')
plt.ylabel('Average Survival Time (ms)')
plt.legend(loc='upper left')
plt.title('Average Survival Time vs. Mg Concentration')
plt.show()
