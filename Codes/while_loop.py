import random

num = random.randint(1, 10)
guess = int(input('Guess a number between 1 and 10'))

# Add while loop here
while (guess != num): 
    if num == guess:
        print('You win!') 
    else :
        guess = int(input('Guess again'))
    
