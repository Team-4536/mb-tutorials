# Using import statements in Python
By the end of this tutorial, you should understand what libraries are, along with how to import them to Python.

## Lets Start with something simple
The keyword `import` lets programs in different files share information. Lets look at an example:

Suppose you have a varible in a file data.py 
```py
fileData: int = 400
```
And program in myProgram.py that contains the following code
```py
coolNumber: float = fileData * 5
print(coolNumber)
```

As it is, running myProgram.py will result in an error, it does not know what the variable fileData is because it is defined in a different file. Import gives us a way to access the fileData variable.

In myProgram.py, if we include an import statement with the name of the file (without the .py)
```py
import data #the name of the file with said variable

# our program below
```
We will have access to the varable `fileData`, but our program still won't work. That's because we need to reference the variable in a special way. Like this:
```py
import data

coolNumber: float = data.fileData * 5
print(coolNumber)
```
Essentially we tell the program to get the ```fileData``` varible _located_ in the file ```data.py```

With import statements, programs can access and use varible, but also functions and classes made in different files.
## What are Libraries?
Now that you know how imports work, we can talk about Libraries. Libraries, or packages, are programs that contain useful code we can utilize in our own programs. Using imports, we can access these useful tools.

When you install python, some libraries come pre-installed on your system and are able to be accessed. The `Math` package is one example and can be used for trig functions and other mathamatical opperations that go beyond common arithmitic.
```py
import math

awesomeNumber = math.sin(math.pi / 2)
```
In this example, both a function, `sin()`, and the variable 

## How do I use them?

## Practice problems
