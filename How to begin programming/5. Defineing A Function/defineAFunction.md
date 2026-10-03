Defining a Function  
Goal: By the end of this tutorial you should be able to define your own functions to run.

Defining a function is the act of making one of those functions you learned how to call in a previous tutorial.

The syntax to create a function is

```py
def functionName(args) -> returnType:
functionBody
```

* def is short for define and indicates that you are about to make a function  
* functionName is what your function will be named such as countDucks  
* args are the arguments that the function takes, such as how print() needs something in its parentheses. Functions may take no arguments, a single augment, or multiple arguments. Arguments may be anything that a variable can be set to such as an integer, string, or custom class  
* \-\> returnType is what the function returns, such as how random.random() gives a random float or other functions that may return things such as strings or integers.  
* functionBody is the code the function actually runs when you call it, this can include basic arithmetic operations, if statements, for loops, and any other code you know.

An example of a function that takes that adds two integers, prints the answer, and returns nothing is.

```py
def addIntegers(int1: int, int2: int) -> None:
	result: int = int1 + int2
	print(result)
```

This is an example of a function that takes in two strings and returns the combination of the strings.

```py
def addString(str1: str, str2: str) -> str:
	addedStr: str = str1 + str2
	return addedStr
```

This is an example of a function that takes in 2 integers and a string and then prints that string an amount of times equal to the sum of the 2 integers, before returning true if the product of the 2 integers is even and false if the product is odd.

```py
def doStuff(printTimes: int, multiplyBy: int, toPrint: str) -> bool:
	summation: int = 0
	isEven: bool = False
	for i in range(printTimes):
		print(toPrint)
	summation = printTimes * multiplyBy
	if(summation % 2 == 0):
		isEven = True
	return isEven
```

Now your turn\!

Define a function that takes in the radius of a circle as a float, prints the area of a circle with that radius, and returns nothing.

Define a function that takes in a string and returns true if one of the following is true

* It contains the letter e  
* It contains the letter o  
* It contains both the letter a and the letter i