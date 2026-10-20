# Before editing this file, make sure that you are in a branch labled as yourName-practice-2026
# If you are not sure you are in that branch ask for help!
aInTex:str = "a"
oIntex:str = "o"
eInTex:str = "e"
iIntex:str = "i"

def thisIsBoring() -> str:
    text:str = input("what do u want to type?: ")
    if eInTex in text:
        print("the letter e is in your text!")
    if oIntex in text:
        print("the letter o is in your text!")
    if aInTex in text:
        if iIntex in text:
            print("the letters a and i are in your text")
thisIsBoring()