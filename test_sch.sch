v {xschem version=2.9.9 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -0 -60 90 -60 { lab=IN}
N 0 -60 -0 -30 { lab=IN}
N 150 -60 200 -60 { lab=OUT}
N 200 -60 200 -30 { lab=OUT}
N 280 -60 280 -30 { lab=OUT}
N 200 -60 280 -60 { lab=OUT}
N 0 30 -0 60 { lab=GND}
N 280 30 280 50 { lab=GND}
N -0 50 280 50 { lab=GND}
N 200 30 200 50 { lab=GND}
C {devices/sqwsource.sym} 0 0 0 0 {name=V1 vhi=3 freq=10e6
}
C {devices/gnd.sym} 0 60 0 0 {name=l1 lab=GND}
C {devices/res.sym} 120 -60 1 0 {name=R1
value=100k
footprint=1206
device=resistor
m=1}
C {devices/res.sym} 200 0 2 0 {name=R2
value=100k
footprint=1206
device=resistor
m=1}
C {devices/capa.sym} 280 0 0 0 {name=C1
m=1
value=10p}
C {devices/lab_pin.sym} 0 -60 0 0 {name=l2 sig_type=std_logic lab=IN}
C {devices/lab_pin.sym} 180 -60 1 0 {name=l3 sig_type=std_logic lab=OUT}
