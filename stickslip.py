##############################
#
# Stick-Slip tool 24.10.2017
#
# Python 2.7 
#
##############################

import numpy as np
import matplotlib.pyplot as plt
import scipy

ifile = open('1_1.ascii', 'r')

dist_tmp = []
shear_stress_tmp = [] 
all_data = ifile


for i,line in enumerate(all_data):
	line = line.rstrip()
	raw_data = line.split('\t')
	dist_tmp.append(raw_data[0])
	shear_stress_tmp.append(raw_data[1])

plt.plot(dist_tmp,shear_stress_tmp)
plt.show()

ifile.close()
