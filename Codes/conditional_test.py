num1 = 10
num2 = 20 

if num1 ==  num2:
    print("equal")
elif num1 > num2:
    print("greater")    
else:
    print("lesser")
    
computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")

if computer_choice == user_choice:
    print("TIE")
elif computer_choice == "rock" and user_choice == "paper":
    print("NO IDEA")
else: 
    print('Lose')
