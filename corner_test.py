"""
VDS and VGS sweep of NMOS from Sky130.
Running over corners
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt
import time

print('Sim started on: ' + time.ctime())
# Load netlist
tic = time.time()
ngspyce.source('corner_test.spice')
toc = time.time()
print(f'ngspice netlist time: {int(toc-tic)} seconds')
# Simulate
tic = time.time()
ngspyce.cmd('tran 10u 10m'.lower())
toc = time.time()
print(f'ngspice sim time: {int(toc-tic)} seconds')

# Read results
time, vcc_v, in_v, out_v, in_i, vcc_i = map(ngspyce.vector, ['time','vcc','in','out','vin#branch','vcc#branch'])

# And plot them
plt.plot(time*1e3, in_v, label='input')
plt.plot(time*1e3, out_v, label='output')

plt.title('BJT amp input and output')
plt.xlabel('Time [ms]')
plt.ylabel('Voltage [V]')
plt.legend()
plt.show()