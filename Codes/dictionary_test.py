#create a dictionary from a list 
product = ['TV', 'Laptop', 'Mobile', 'Drawing Pad']
inventory = {}
price = 12

for i in product: 
    inventory[i] = price
    price += 10

#print key value pair 
for key, value in inventory.items():
    print(key,value)
