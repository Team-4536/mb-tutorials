X:str=("4536")
B:str=input("Guess a number:  ")
if B == X:
    print("Correct!! You are the Best!")
else:
    print("Wrong!! Two guesses left!!")
    L=input("Guess a number:  ")
    if L == X:
        print("Correct!! You are the Best!")
    else:
        print("WRONG!!!!!! ONE GUESS LEFT !! !! ! ")
        C=input("GUEESS A NUMBER ITS YOUR LAST CHANCE !!!!!!!    ")
        if C == X:
            input("Nice save! press enter to close.")
        else:
            print("WRONG YOU POOPYHEAD!!!!!!!!!")