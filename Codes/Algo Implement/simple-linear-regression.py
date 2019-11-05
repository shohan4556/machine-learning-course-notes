import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

# data 
xx = [0,1,2,3,4,5,6,7,8,9]
yy = [1,3,2,5,7,8,8,9,10,12]

# mean / average 
xx_mean = np.mean(xx)
yy_mean = np.mean(yy)

# total number of value 
n = len(xx)

up = 0
down = 0

for i in range(n):
  up += (xx[i] - xx_mean) * (yy[i] - yy_mean)
  down += (xx[i] - xx_mean) **2

m = up/down  
c = yy_mean - (m * xx_mean)

print(m, c) # now calculate (y1...yn = m(x1...xn)+c) for each value of

# calculate y1....yn
YY = []

for i in range(n):
  tmp = m * xx[i] + c
  YY.append(tmp)


# ploting regression line 
plt.scatter(xx,yy)
plt.plot(xx,YY)

plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.grid(True)
plt.show()

