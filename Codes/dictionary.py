performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2.00pm', 
                'Enchanted Elephants':'5.00pm'
                }

if performances.get('showtime') == None:
    print("Performance doesn't exist")
else : 
    print('The time of the Bearded Lady show is')
    
# two list must be same value and same order to check     
#print(performances.get('Snake Charmer'))