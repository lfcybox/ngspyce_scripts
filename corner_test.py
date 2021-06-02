"""
Simple testbench to run corners.
The netlist placeholde SIM_BJTCORNER is modified
on this script to run different corners
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt

netlist_file = 'corner_test.spice'
corners = ['typ','betalow']


for corner in corners:
	# Read and modify netlist
	with open(netlist_file,'rt') as netlist:
		ngspyce.circ(netlist.read().replace('SIM_BJTCORNER',corner))

	# Simulate
	ngspyce.cmd('tran 10u 10m'.lower())

	# Read results
	time, vcc_v, in_v, out_v, in_i, vcc_i = map(ngspyce.vector, ['time','vcc','in','out','vin#branch','vcc#branch'])

	# And plot them
	plt.figure(corner)
	plt.plot(time*1e3, in_v, label='input')
	plt.plot(time*1e3, out_v, label='output')

	plt.title('BJT amp input and output -' + corner)
	plt.xlabel('Time [ms]')
	plt.ylabel('Voltage [V]')
	plt.legend()

	plt.figure('combined')
	plt.plot(time*1e3, in_v, label='input '+corner)
	plt.plot(time*1e3, out_v, label='output '+corner)
	plt.title('BJT amp input and output combined')
	plt.xlabel('Time [ms]')
	plt.ylabel('Voltage [V]')
	plt.legend()

plt.show()