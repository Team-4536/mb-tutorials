# if statement practice 
import random 


numbers = ["1", "2", "3"]
guess = input("guess a number 1-3: " )
number = random.choice(numbers)
# print(number)

if number == guess:
    print()
    print("CORRECT")
    print("the number was: ", number)
    print()
else:
    print()
    print("WRONG")
    print("the number was: ", number)
    print()