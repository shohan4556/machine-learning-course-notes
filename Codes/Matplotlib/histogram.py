import matplotlib.pyplot as plt

value = [0.1,0.25,0.3,0.95,0.45,1,4,4.2,3.2,2.5,4.4]
#if does not specify bins default value will be 10
plt.hist(value, bins=3)
plt.show()

#clean plot 
#plt.clf()
