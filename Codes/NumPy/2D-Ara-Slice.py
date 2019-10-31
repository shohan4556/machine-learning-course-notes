import numpy as np 

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

print(np_baseball.shape)
print(type(np_baseball))

#slicing 
#a[start:stop] 
#items start through stop-1
#a[start:stop:step]

print('Only second row : ',np_baseball[1,:])

print('Only second column : ',np_baseball[:,1])

print('2nd and 3rd row : ',np_baseball[1:3])