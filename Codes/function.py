def Average(num):
    total = 0
    for i in num:
        total += i
    #local scope     
    avg = total / len(num)
    return avg


price = [1,2,3,4,5,6]

#global scope
avg = Average(price)

print(avg)