##############################
#
# Stick-Slip tool 24.10.2017
#
# Florian Petersen and Robert Kurzawski MYLONITE
#
# Python 2.7
#
##############################
#!/usr/bin/python2.7
# coding: latin-1

import numpy as np
import glob
import matplotlib.pyplot as plt
import scipy.optimize as optimization
from scipy import stats

##################
## Functions
##################

## Moving average
def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

##################
## Start of File
##################

## load File

a = []
b_up = []
disp_b_up = []
b_down = []
disp_b_down = []
stress_buildup = []
stress_drop = []
xfile = []
xfile = glob.glob('1_1.ascii')
xfile.sort()
for M, data in enumerate(xfile):
    print data
    all_data = []
    ifile = open(data,'r')
    all_data = ifile
    disp = []
    shear_stress = []
    for i,line in enumerate(all_data):
		line = line.rstrip()
		raw_data = line.split('\t')
		disp.append(float(raw_data[0]))
		shear_stress.append(float(raw_data[1]))

## Running average to smooth Data

    #f1 = plt.figure(1)
    #plt.plot(disp,shear_stress)


    shear_stress = movingaverage(shear_stress,2)
    disp = movingaverage(disp,2)


    #plt.plot(disp,shear_stress)
    #f1.show()

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



    for i in range(0, len(picks)):
        if i != (len(picks)-1):
            event = shear_stress[picks[i]:picks[i+1]]
            if len(event) >= 3:
                if (event[0]-event[1]) < 0:
                    print ' New slope '
                    print i
                    x = disp[picks[i]:picks[i+1]]
                    y = event
                    stress_buildup.append(disp[picks[i+1]] - disp[picks[i]])
                    for j in range(3,len(x)):
                        xy_corr = np.corrcoef(x[0:j],y[0:j])
                        #print xy_corr
                        #print x[0:j],y[0:j]
                    slope_tmp, intercept_tmp, r_value_tmp, p_value_tmp, std_err_tmp = stats.linregress(x,y)
                    b_up.append(slope_tmp)
                    disp_b_up.append(x[0])


                if (event[0]-event[1]) > 0:

                    x = disp[picks[i]:picks[i+1]]
                    stress_drop.append(disp[picks[i+1]] - disp[picks[i]])
                    y = event
                    slope_tmp, intercept_tmp, r_value_tmp, p_value_tmp, std_err_tmp = stats.linregress(x,y)
                    b_down.append(slope_tmp)
                    disp_b_down.append(x[0])

	peak_plt = []
	n = 0
	for h in disp:
		if peak[n] == h:
			peak_plt.append(h)
			if n >= (len(peak)-1):
				continue
			n=n+1
		else:
			peak_plt.append(0)


	ifile.close()
#fig2 = plt.figure(7)
#plt.plot(disp_b_down,np.array(b_down),'.')
#fig2.show()
#b = plt.figure(2)

#for xc in peak_plt:
#    plt.axvline(x=xc)
#plt.plot(disp,shear_stress-np.mean(shear_stress))
#b.show()
