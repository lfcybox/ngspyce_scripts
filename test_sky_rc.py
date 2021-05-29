"""
Transient test of RC with Sky130 components.
Netlist generated with xschem. Does not include any ngspice command
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt

# Load netlist
ngspyce.source('test_sky_rc.spice')
# Simulate 10 ms
ngspyce.cmd('tran 1n 1u uic')

# Read results
time, IN, OUT = map(ngspyce.vector, ['time', 'IN', 'OUT'])
# And plot them
plt.plot(time*1e3, IN, label='IN')
plt.plot(time*1e3, OUT, label='OUT')

plt.title('RC transient')
plt.xlabel('Time [ms]')
plt.ylabel('Voltage [V]')
plt.savefig('test_sky_rc.png')
plt.show()
