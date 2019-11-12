# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)

# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100)) #since the number is so large it wil exceed memory 

print('iter',next(googol))