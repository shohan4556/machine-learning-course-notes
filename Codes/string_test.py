greeting = "G'day-mate."
name = "shohan"
description = "Happy new year "
year = 2020
sentence = description + str(year) + " " +name 

print(sentence)

movie1 = "\n\tAkira"
movie2 = "\n\tThe Necessary Death of Charlie Countryman"

print("My Favorite Movies: "+movie1+movie2)

#library function 
print(type(movie1))

#library function
print(len(sentence))

#substring print 
print(name[1:4])

#middle character of greeting 
#integer division 
mid = len(greeting)//2 
print(greeting[mid])


word = 'Python'
first = word[0]
rest = word[1:]
result = rest + '-'+first+'y'
print(result)
