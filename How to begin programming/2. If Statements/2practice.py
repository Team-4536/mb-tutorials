M=str("minutebots")or("Minutebots")or("MinuteBots")
G=input("say the magic word")
if (G == M):
    input("Correct!! press enter to close.")
else:
    N=input("WRONG!! Two guesses left: ")

if (N == M):
    input("Correct!! press enter to close.")
else:
    H=input("WRONG AGAIN!! ONE GUESS LEFT!!!:")

if (H == M):
    input("Correct!! press enter to close.")
else:
    print("WRONG!!!! YOU LOSE!!")
    print(" ")
    print(" ")
    input("press enter to close.")