import numpy as np
import scipy
import scipy.signal
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from astropy.io import ascii
from astropy.io import fits
from astropy.table import Table, Column

dir = '/users/fastforward/desktop/'
file = 'cosmoscatalog_v2.csv'
fname = dir + file

cols = np.loadtxt(fname, delimiter=',', skiprows=1, dtype=('d'),usecols=range(0,25),unpack=True)
#converts columns 0 to 25 of the csv file to doubles. to call a column use cols[0-25]
comments = np.loadtxt(fname, delimiter=',', skiprows=1, dtype=('str'), usecols=(26,), unpack=True)
#keeps comments as strings but puts them in an array called comments
floats = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=range(27,55),unpack=True)
#converts columns 27 to 55 of the csv file to doubles. to call a column use floats[0-29]

uvrest = floats[22] - floats[24]
vjrest = floats[24] - floats[27]


e = floats[0]==0. # gives boolean array where true indicates ellipticals
s = floats[0]==1. # boolean array for spirals
i = (cols[6]==1 or cols[9]==1 or cols[10]==1)
dd = floats[0]==0. # gives boolean array where true indicates ellipticals
bd = floats[0]==1. # boolean array for spirals


plt.figure()
plt.subplot()
plt.plot(vjrest[s],uvrest[s],'bo', ms=3, mec='b')
plt.plot(vjrest[e],uvrest[e],'ro', ms=3, mec='r')
plt.plot([0.0,1.7,2.3,2.3], [0.775,0.775,1.0,1.2], color='black')

#Axis Labels and Title
plt.ylabel("U-V")
plt.xlabel("V-J")

#Legend
red_patch = mpatches.Patch(color='r', label='The red data')
blue_patch = mpatches.Patch(color='b', label='The blue data')
plt.legend([red_patch, blue_patch], ["Elliptical", "Spiral"])

#end
