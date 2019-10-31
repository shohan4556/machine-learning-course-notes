import numpy as np

height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69]
weight = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180, 188, 180, 185, 160, 180]

# bmi 
# weight kg / height * height m
# calcuale bmi 
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height **2 
print("BMI of All baseball players ",bmi)

#lightweight player
lightweight = bmi >= 0.04

print('Light Weight Player ',bmi[lightweight])