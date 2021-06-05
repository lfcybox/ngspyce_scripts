"""
Improved testbench to run corners.
This attempts to be an example on how to run many
simulations while taking care of memory usage.
destroy all command will release the memory holding data.
This includes the data read using ngspyce.vector().
remcirc removes the current circuit.
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt

netlist_file = 'corner_test_improved.spice'
# corners = ['typ','betalow']
corners = ['corner'+str(x) for x in range(1,101)]


for corner in corners:
	# Read and modify netlist
	with open(netlist_file,'rt') as netlist:
		ngspyce.circ(netlist.read().replace('SIM_BJTCORNER','typ'))

	# Simulate
	ngspyce.cmd('tran 10u 10m'.lower())

	# Read results
	time, vcc_v, in_v, out_v, in_i, vcc_i = map(ngspyce.vector, ['time','vcc','in','out','vin#branch','vcc#branch'])

	# And plot them
# 	plt.figure(corner)
# 	plt.plot(time*1e3, in_v, label='input')
# 	plt.plot(time*1e3, out_v, label='output')

# 	plt.title('BJT amp input and output -' + corner)
# 	plt.xlabel('Time [ms]')
# 	plt.ylabel('Voltage [V]')
# 	plt.legend()

	plt.figure('combined')
	plt.plot(time*1e3, in_v, label='input '+corner)
	plt.plot(time*1e3, out_v, label='output '+corner)
	plt.title('BJT amp input and output combined')
	plt.xlabel('Time [ms]')
	plt.ylabel('Voltage [V]')
	# plt.legend()
	
	print('\n'.join(ngspyce.cmd('rusage'))+'\n')
	
	# Free memory
	# I think ngspyce.vector() is a pointer to the data, but does not make copies. 
	# Using 'destroy all' would remove that data and the numpy arrays would be gone
	# You can do 'destroy all' once the vectors are no longer needed...
	ngspyce.cmd('destroy all') 
	# ngspyce.cmd('reset')
	ngspyce.cmd('remcirc')

plt.show(block=False)
