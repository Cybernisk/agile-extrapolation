import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import polyval, polyfit, interpolate

NEW_POINTS_COINT = 6

data = np.array([[1,1134], [2,1084], [3,993.5], [4,799.5]])
# fast decreace
#data = np.array([[1,1134], [2,400], [3,399.5], [4,100.5]])
# increase
#data = np.array([[1,799], [2,854], [3,999.5], [4,1000.5]])

# average data
avr = np.average(data)

# make a polifit to data and create polynom
fit = np.polyfit(data[:,0], data[:,1] ,1)
line = np.poly1d(fit)

# create x points
new_points = np.arange(NEW_POINTS_COINT)+5

# create y points
new_y = line(new_points)

# trim any zero values
new_y[new_y < 0 ] = 0

# create a noise data like average
noise = np.random.normal(new_y,scale=(avr/10), size=len(new_y))

# if we have some errors in noise we must no have values below zero
noise[noise < 0] = 0

# new y with noise data
new_ywn = noise

# Create a poly exrtapolated data line
data_line = np.stack((new_points, new_y), axis=-1)
data_line = np.append(data, data_line, axis=0)

# add stack created data and added it to initial data
data2 = np.stack((new_points, new_ywn), axis=-1)
data3 = np.append(data[3:], data2, axis=0)

# slice it to one axis
data4=data3[:,1]

# lets delete any points under X axis and trim it at end
data4[data4 <0] = 0
data_z = np.where(data4 ==0)[0]
if data_z.any():
    data5 = (data4[:data_z[0]+1])
else:
    data5 = data4

# final data and final plot
print(data5, data_line, len(data5)+1)
plt.plot(data[:,0], data[:,1],'r', data3[:,0], data3[:,1], 'green', data_line[:,0], data_line[:,1], 'r--')
