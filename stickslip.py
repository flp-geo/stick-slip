##############################
#
# Stick-Slip tool 24.10.2017
#
# Florian Petersen
#
# Python 2.7 
#
##############################
#!/usr/bin/python
# coding: latin-1

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.optimize as optimization

## Functions
def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

def func(x, a, b):
    return a + b*x

## load file

ifile = open('1_1.ascii', 'r')

disp = []
shear_stress = [] 
all_data = ifile


for i,line in enumerate(all_data):
	line = line.rstrip()
	raw_data = line.split('\t')
	disp.append(float(raw_data[0]))
	shear_stress.append(float(raw_data[1]))

fig = plt.figure(1)
plt.plot(disp,shear_stress)
fig.show()
ifile.close()


## Running average to smooth Data

shear_stress = movingaverage(shear_stress,2)
disp = movingaverage(disp,2)

## Derivation with moving slope

dY = (np.roll(shear_stress, -1, axis=0) - shear_stress)[:-1]
dX = (np.roll(disp, -1, axis=0) - disp)[:-1]

shear_stress = np.roll(shear_stress, -1, axis=0)[:-1]
disp = np.roll(disp, -1, axis=0)[:-1]

slopes = dY/dX

## Pick peaks of zero slope

picks = np.where(np.diff(np.sign(slopes)))[0]

## Picks to peak posisitons in Displacement

peak = disp[picks]

a = []
b = []
disp_b = []
for i in range(0, len(picks)):
	if i != (len(picks)-1):
		event = shear_stress[picks[i]:picks[i+1]]
		if len(event) > 5:
			print len(event)
			if (event[0]-event[1]) < 0: 
				x = disp[picks[i]:picks[i+1]]
				y = event
				least_square = np.polyfit(x, y, 1)
				a.append(least_square[0])
				b.append(least_square[1])
				disp_b.append(x[0])
fig2 = plt.figure(2)
plt.plot(disp_b,b,'.')
fig2.show()

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
	

#b = plt.figure(2)

#for xc in peak_plt:
#    plt.axvline(x=xc)
#plt.plot(disp,shear_stress-np.mean(shear_stress))
#b.show()


