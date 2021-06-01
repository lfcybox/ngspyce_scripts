"""
VDS and VGS sweep of NMOS from Sky130.
Running over corners
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt
import time

print('Sim started on: '+time.ctime())
# Load netlist
tic = time.time()
ngspyce.source('nmos_tb.spice')
toc = time.time()
print(f'ngspice netlist time: {int(toc-tic)} seconds')
# Simulate
tic = time.time()
ngspyce.cmd('dc Vd 0 1.8 0.1 Vg 0 1.8 0.3'.lower())
toc = time.time()
print(f'ngspice sim time: {int(toc-tic)} seconds')

# Read results
vd, vg, ids, gm = map(ngspyce.vector, ['d', 'g', '@m.xm1.msky130_fd_pr__nfet_01v8_lvt[id]','@m.xm1.msky130_fd_pr__nfet_01v8_lvt[gm]'])

# reshape. Make the first dimension match the length of 2nd sweep (Vg)
vd = vd.reshape(7,-1).transpose()
vg = vg.reshape(7,-1).transpose()
ids = ids.reshape(7,-1).transpose()
gm = gm.reshape(7,-1).transpose()
# At this point gm index is gm[Vd , Vg] such that gm[:,0] is a vector of gm for each Vd for the first Vg value

# Plot ids vs vds, vg sweep
plt.figure(1)
for param in vg[0,:]:
    plt.plot(vd[vg == param], ids[vg == param], '-',
             label='Vg = {:.1f}'.format(param))

plt.legend(loc='center right')
plt.title('Output characteristics for Sky130 NMOS')
plt.xlabel('VDS [V]')
plt.ylabel('IDS [A]')
#plt.savefig('bc337.png')


# plot ids vs vgs, vds sweep
plt.figure(2)
for param in vd[:,0]:
    plt.semilogy(vg[vd == param], ids[vd == param], '-',
             label='Vd = {:.1f}'.format(param))

plt.ylim(bottom=1e-12)
plt.legend(loc='center right')
plt.title('Output characteristics for Sky130 NMOS')
plt.xlabel('VGS [V]')
plt.ylabel('IDS [A]')

plt.show()