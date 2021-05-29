"""
DC sweep test.
Netlist generated with xschem. Does not include any ngspice command
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt

# Load netlist
ngspyce.source('test_sch2.spice')
# Simulate 10 ms
ngspyce.cmd('dc V1 0 1 0.1 V2 0 1 0.2'.lower()) # note the lowercase

# Load simulation results into numpy arrays
IN1, IN2, OUT = map(ngspyce.vector, ['IN1', 'IN2', 'OUT'])

plt.figure()
# Plot one line per IN1 voltage
series = np.unique(IN1)
for _in1 in series:
    plt.plot(IN2[IN1 == _in1], OUT[IN1 == _in1], '-',
             label='IN1 = {:.1f}'.format(_in1))

plt.legend(loc='center right')
plt.title('OUT vs IN2 for different IN1')
plt.xlabel('IN2 [V]')
plt.ylabel('OUT [V]')
plt.savefig('test_sch2.png')
plt.show()
