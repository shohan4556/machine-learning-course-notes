# zip(list1, list2): combine two list and make a touple 
vehicles = ['unicycle', 'motorcycle', 'plane', 'car', 'truck']
wheels = [1, 2, 3, 4, 18]

touple = list(zip(vehicles, wheels))

#print(touple)

for i,j in touple: 
    print(i, j)

# to split touple 
print(*touple)
