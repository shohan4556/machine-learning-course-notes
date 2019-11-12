vehicles = ['unicycle', 'motorcycle', 'plane', 'car', 'truck']
wheels = [1, 2, 3, 4, 18]

touple = list(zip(vehicles, wheels))

#print(touple)

for i,j in touple: 
    print(i, j)

print(*touple)