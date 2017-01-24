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

dist = []
shear_stress = [] 
all_data = ifile


for i,line in enumerate(all_data):
	line = line.rstrip()
	raw_data = line.split('\t')
	dist.append(float(raw_data[0]))
	shear_stress.append(float(raw_data[1]))

plt.plot(shear_stress)

ifile.close()

for i in dist
	dY=i[]


dY = (np.roll(shear_stress, -1, axis=0) - shear_stress)[:-1]
dX = (np.roll(dist, -1, axis=0) - dist)[:-1]

slopes = dY/dX

for x, y  in enumerate(slopes):
	if y == 0:
		print dist[x]

plt.plot(slopes)
plt.show()
