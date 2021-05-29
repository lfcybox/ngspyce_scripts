v {xschem version=2.9.9 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 0 -60 90 -60 { lab=IN1}
N 0 -60 0 -30 { lab=IN1}
N 150 -60 200 -60 { lab=OUT}
N 0 30 0 60 { lab=GND}
N 200 10 200 30 { lab=IN2}
N 0 60 0 90 { lab=GND}
N 0 90 -0 100 { lab=GND}
N 200 -60 200 -50 { lab=OUT}
N -0 90 200 90 { lab=GND}
C {devices/gnd.sym} 0 100 0 0 {name=l1 lab=GND}
C {devices/res.sym} 120 -60 1 0 {name=R1
value=100k
footprint=1206
device=resistor
m=1}
C {devices/res.sym} 200 -20 2 0 {name=R2
value=50k
footprint=1206
device=resistor
m=1}
C {devices/lab_pin.sym} 0 -60 0 0 {name=l2 sig_type=std_logic lab=IN1}
C {devices/lab_pin.sym} 180 -60 1 0 {name=l3 sig_type=std_logic lab=OUT}
C {devices/vsource.sym} 0 0 0 0 {name=V1 value=3}
C {devices/vsource.sym} 200 60 0 0 {name=V2 value=3}
C {devices/lab_pin.sym} 200 20 0 0 {name=l4 sig_type=std_logic lab=IN2
}
