def average(num):
    total = 0
    for i in num:
        total += i
        
    avg = total / len(num)
    return avg 
    

#not necessary but best practice 
def main():
    price = [1,20,30,33,56]
    price_avg = average(price)
    print(price_avg)
    
main()
