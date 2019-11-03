import matplotlib.pyplot as plt

year = [10,20,30,40,50]
pop = [1,2,3,4,5]

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

plt.xlabel("year")
plt.ylabel("population")
plt.title("world population")
plt.yticks([2,4,6,8,10],
          ['0B','2B','4B','6B','8B'])
          
plt.grid(True)
# Display the plot with plt.show()
plt.show()