#This tutorial is to teach new or educate already
#expierienced python coders on use of VScodes python Debugger.

R=3
print()
print("a purposefully bad input example is about to start. the correct number is 3.")
K=input("enter a number 1 - 5:    ")

if K == R:
    input("congratulations! if you are seeing this, the tutorial didnt work. press enter to close.")
else:
    print("wrong!! if you are seeing this despite entering the right number, the tutorial is working")

L=input("second try:   ")

if L == R:
    input("If you are seeing this, the tutorial must hve somehow corrected itself.")
else:
    print("ok good the tutorial has worked. now open VScode and use debugger. press enter to close.")