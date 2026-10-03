# **Calling a function in Python**

*Goal: You should be able to call any function in Python*

# What are Functions?

Functions are prewritten code with unique names, they run when they are called.  
Think of a function like the name of a task (like cleaning the dishes). Your parents can just yell “clean the dishes\!” instead of having to explain how to wipe them down each time. Same with a function. Instead of rewriting a complex task in code over and over, you can turn that task into a function and call it with just one line\!

Sometimes you might want a function to act slightly differently depending on the parameters of the specific situation. For example, your parents might yell “clean the dishes by 5 \!” or “clean the dishes by 4 \! ” Programmers use the word “arguments” when describing these parameters (in this scenario, the argument is the time the dishes need to be cleaned).

You also might want to get some information back from a function about what happened when it ran. For example, your parents yell to you “clean the dishes by 5 \!” And after you finish cleaning, you might yell back “I only broke 2 plates\!” In programming, this is called returning a value. Braking 2 plates would be the returned value in this scenario.

# Function syntax

The syntax for calling a function in Python is:

```py
returnedValue = functionName(argument)
```

Functions can also have more than one arguments, or more than one returned value that would look like:

```py
returnedValue1, returnedValue2,... = functionName(argument1, argument2, …)
```

### 

In our dishes example, calling the function would look like this:

```py
platesBroken = cleanTheDishes(5)
```

### 

which translates to: “Clean the dishes by 5 \!” and then the amount of plates broken is saved in the variable “platesBroken”

Arguments can be variables too:

```py
timeToCleanDishesBy = 5
platesBroken = cleanTheDishes(timeToCleanDishesBy)
```

### 

Depending on the function, arguments, and the returned value could be any variable type (string, integer, etc…)

# How do I use one?

In a later tutorial (Defining a function) you will learn how to make your own function. For now though, we will focus on Python’s built-in functions. You can find a full list of them linked [here](https://www.w3schools.com/python/python_ref_functions.asp)  
	The two functions we will focus on are `input()` and `print()`

```py
input()
```

### 

The user types something into the console, what is typed is then returned.   
Arguments: none  
Returned Value: What is typed in the console

```py
print()
```

### 

Prints the arguments to the console.  
Arguments: what you want to print to the console, this can be strings and ints, as well as some lists  
Returned value:none

example:

```py
print("hello world")
text = input()
```

### Try running this code, it will print the words “hello world” to the console, and then it lets the user input some text.(note: after writing the text you have to press the enter key) it then saves that text to the “text” variable

## Practice problems:

1. Make the console say your name.  
2. Write text to the console, then have it say that back.  
3. Have the console ask for your name, then let you type your name , then say “hello \_\_”(your name)

