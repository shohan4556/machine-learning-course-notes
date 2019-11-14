# list comprehension creates an entire list 
# generator does not creates list instead creates generator objects 

# Create list comprehension: squares
# list comprehension
squares = [i **2 for i in range(0,10)]
print(squares)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member for member in fellowship if len(member) >= 7]

print(new_fellowship)


# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
# generator 
lengths =(len(person) for person in lannister)
print(type(lengths))

# Iterate over and print the values in lengths
for value in lengths:
    print(value)