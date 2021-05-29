v {xschem version=2.9.9 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 1770 -1710 1770 -1670 { lab=IN}
N 1770 -1710 1820 -1710 { lab=IN}
N 1880 -1710 1930 -1710 { lab=OUT}
N 1930 -1710 1930 -1670 { lab=OUT}
N 1930 -1610 1930 -1580 { lab=GND}
N 1770 -1580 1930 -1580 { lab=GND}
N 1770 -1610 1770 -1580 { lab=GND}
N 1930 -1710 2040 -1710 { lab=OUT}
N 2040 -1710 2040 -1680 { lab=OUT}
N 2040 -1620 2040 -1580 { lab=GND}
N 1930 -1580 2040 -1580 { lab=GND}
C {devices/gnd.sym} 1840 -1580 0 0 {name=l1 lab=GND}
C {devices/lab_pin.sym} 1930 -1710 1 0 {name=l2 sig_type=std_logic lab=OUT}
C {sky130_fd_pr/cap_mim_m3_1.sym} 2040 -1650 0 0 {name=C1 model=cap_mim_m3_1 W=10 L=10 MF=2 spiceprefix=X}
C {devices/sqwsource.sym} 1770 -1640 0 0 {name=V1 vhi=3 freq=10e6
}
C {sky130_fd_pr/res_xhigh_po.sym} 1930 -1640 0 0 {name=R2
W=1
L=1000
model=res_xhigh_po
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po.sym} 1850 -1710 3 0 {name=R3
W=1
L=1000
model=res_xhigh_po
spiceprefix=X
mult=1}
C {devices/gnd.sym} 1850 -1690 0 0 {name=l3 lab=GND}
C {devices/gnd.sym} 1850 -1690 0 0 {name=l4 lab=GND}
C {devices/gnd.sym} 1910 -1640 1 0 {name=l5 lab=GND}
C {devices/lab_pin.sym} 1770 -1710 1 0 {name=l6 sig_type=std_logic lab=IN}
C {devices/code_shown.sym} 1750 -1940 0 0 {name=CORNER
only_toplevel=true
format="tcleval( @value )"
value="
.temp 27
.lib \\\\$::SKYWATER_MODELS\\\\/models/sky130.lib.spice tt
*.lib \\\\$::SKYWATER_MODELS\\\\/models/sky130.lib.spice ss
*.lib \\\\$::SKYWATER_MODELS\\\\/models/sky130.lib.spice ff
*.lib \\\\$::SKYWATER_MODELS\\\\/models/sky130.lib.spice sf
*.lib \\\\$::SKYWATER_MODELS\\\\/models/sky130.lib.spice fs
"}
