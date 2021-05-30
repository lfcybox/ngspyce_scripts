# Running the examples

The examples can be run as:

python3 test_sch.py

It will run the netlist test_sch.spice and return a plot (also saved as test_sch.png)

# ngspyce
Clone: https://github.com/ignamv/ngspyce

Then cd into the repo

sudo python3 setup.py install

# ngspice shared library
See https://ignamv.github.io/ngspyce/#getting-libngspice for how to install ngspice as shared library, or alternatively see https://github.com/lfcybox/sky130_setup install_tools.sh (in particular, the lines where ngspice is installed using --with-ngshared)
