"""
Simple testbench to run corners.
The netlist placeholde SIM_BJTCORNER is modified
on this script to run different corners
"""

import ngspyce
import numpy as np
from matplotlib import pyplot as plt
from itertools import product

netlist_file = 'param_test.spice'
corners = ['typ','betalow']
params_rc = ['10k','50k','100k'] # for now, hardcoded to a known parameter and strings
params_rb = ['68k','20k']

for corner, param_rc , param_rb in product(corners,params_rc,params_rb):
	sweep_name = f'corner {corner}, RC {param_rc}, RB {param_rb}'
	print(f'Running '+sweep_name+'\n')
	# Read and modify netlist
	with open(netlist_file,'rt') as netlist:
		ngspyce.circ(netlist.read().replace('SIM_BJTCORNER',corner))

# FROM NGSPYCE CODE
# def alterparams(**kwargs):
#     for k, v in kwargs.items():
#         cmd('alterparam {} = {}'.format(k, v))
#     cmd('reset')

	ngspyce.alterparams(rc=param_rc,rb=param_rb)

	# Simulate
	ngspyce.cmd('tran 10u 10m'.lower())

	# Read results
	time, vcc_v, in_v, out_v, in_i, vcc_i = map(ngspyce.vector, ['time','vcc','in','out','vin#branch','vcc#branch'])

	# And plot them
	# plt.figure(corner)
	# plt.plot(time*1e3, in_v, label='input')
	# plt.plot(time*1e3, out_v, label='output')

	# plt.title('BJT amp input and output -' + corner)
	# plt.xlabel('Time [ms]')
	# plt.ylabel('Voltage [V]')
	# plt.legend()

	plt.figure('combined')
	plt.plot(time*1e3, in_v, label='input '+sweep_name)
	plt.plot(time*1e3, out_v, label='output '+sweep_name)
	plt.title('BJT amp input and output combined')
	plt.xlabel('Time [ms]')
	plt.ylabel('Voltage [V]')
	plt.legend()

	# Free memory
	# I think ngspyce.vector() is a pointer to the data, but does not make copies. 
	# Using 'destroy all' would remove that data and the numpy arrays would be gone
	# You can do 'destroy all' once the vectors are no longer needed...
	# ngspyce.cmd('destroy all') 
	ngspyce.cmd('remcirc')

plt.show(block=False)