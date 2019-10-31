def SaveOrder(orderDict):
    file = open("orderLog.txt", 'w')
    total = 0 
    
    for item, price in orderDict.items():
        file.write(item+'-->'+str(price)+'\n')
        total += price
    
    file.write('Total = '+str(total))
    file.close()
    
def main():
    order = {
        'Pizza':100,
        'Snaks':200,
        'Pasta':500,
        'Coke' :50
    }
    
    SaveOrder(order)
    print("Log successfully added")
    
    
main()
