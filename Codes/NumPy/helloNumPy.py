import numpy as np

salary = [10,15,20,35,65]
np_array = np.array(salary)

print(type(np_array))

#comparison 
print(np_array > 22)

#numpy subsetting 
print(np_array[np_array>50])

