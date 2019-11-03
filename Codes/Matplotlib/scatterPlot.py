import matplotlib.pyplot as plt

year = [10,20,30,40,50]
pop = [1,2,3,4,5]

plt.xscale('log')

plt.scatter(year,pop)
plt.show()