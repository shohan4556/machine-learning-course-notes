myorder = []
menu = {
    "Bean":120,
    "Steak":500,
    "Squide":600
}

order = input("Enter menu item, for Quit press Q")

while (order.upper() != 'Q'):
    found = menu.get(order)
    
    if found:
        myorder.append(found)
    else:
        print("menu item does not exit")
        
    order = input("Want to add more or press Q to exit")


print(myorder)
#output : [120,600]
