##############################
#
# Stick-Slip tool 24.10.2017
#
# Florian Petersen
#
# Python 2.7 
#
##############################

import numpy as np
import matplotlib.pyplot as plt
import scipy

ifile = open('1_1.ascii', 'r')

disp = []
shear_stress = [] 
all_data = ifile


for i,line in enumerate(all_data):
	line = line.rstrip()
	raw_data = line.split('\t')
	disp.append(float(raw_data[0]))
	shear_stress.append(float(raw_data[1]))

a = plt.figure(1)
plt.plot(disp,shear_stress)
a.show()
ifile.close()

## Derivation with moving slope

N=5
disp_mean = np.convolve(disp, np.ones((N,))/N)[(N-1):]

dY = (np.roll(shear_stress, -1, axis=0) - shear_stress)[:-1]
dX = (np.roll(disp, -1, axis=0) - disp)[:-1]

shear_stress = np.roll(shear_stress, -1, axis=0)[:-1]
disp = np.roll(disp, -1, axis=0)[:-1]


slopes = dY/dX

## Pick peaks of zero slope

picks = np.where(np.diff(np.sign(slopes)))[0]

## Picks to peak posisitons in Displacement


peak = disp[picks]

peak_plt = []
n = 0
for x in disp:
	if peak[n] == x:
		peak_plt.append(x)
		if n >= (len(peak)-1):
			continue
		n=n+1
	else:
		peak_plt.append(0)		
	

b = plt.figure(2)
for xc in peak_plt:
    plt.axvline(x=xc)
plt.plot(disp,shear_stress-np.mean(shear_stress))
b.show()
