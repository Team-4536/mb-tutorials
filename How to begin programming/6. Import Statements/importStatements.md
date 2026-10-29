<style>
code, pre{
    white-space: pre !important;
    overflow-x: auto !important;
}
</style>
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

## How do I use them?
When you install python, some libraries come pre-installed on your system and are able to be accessed. The `math` package is one example and can be used for trig functions and other mathamatical opperations that go beyond common arithmitic.
```py
import math

awesomeNumber = math.sin(math.pi / 2)
```
In this example, both a function, `sin()`, and the variable `pi` are from the `math` library and we are accessing them by referencing `math` and the name of said funtion or variable. Usually when accessing a varible from another file, it is to access a constant; in this case, `math.pi` accesses the constant `pi`.

Most libraries we use for our robot have to be installed externally, but once installed, they are accessed the same way.

## Additional Cool Things
There is some more syntax that can be utilized when dealing with `import` that can be useful in certain situations.

### The "`from`" Keyword
When writing a statement like:
```py
import math
```
we are giving the current file access to the entity of the `math` package. This is not always neccisary or wanted. It's also the case that when trying to access a variable or function, we have to tell the program to 'search' the library for a variable or function with that name, like `math.sin()`.

The '`from`' keyword can be utilized to change both of these, 'inconvieninces' if you will. Consider the code below
```py
from math import sin
```
Putting the syntax into english, it says "from the `math` file, give me access to variable or function named '`sin`' (in this case, it would be the `sin()` function). A couple things change when impoting like this. First, we no longer have to write `math.sin()` in order to access the function, we can simply write `sin()`.
```py
from math import sin

coolNumber: float = sin(1.57)
```
However, their is a consequnce to using this form of import, we can only access from `math` what we specifically say. For instance, we can no longer access `math.pi` with this method
```py
from math import sin

PI: float = math.pi # does not work!
```
How we could fix this is simply by including `pi` in the list of things we want to import by seperating it with a comma
```py
from math import sin, pi

coolNumber: float = sin(pi)
```
When importing a few variables and functions like this, this is a fine way to do it, but if we had 20 variables and 10 functions we wanted to use, fitting it all on one line becomes less than ideal. Instead we can use this syntax to sperate each variable or function vertically:
```py
from math import (
    sin,
    pi, # optional trailing comma
)
```

Now, technically you can combine a general import with an explicit import to make certain things accesible without explicitly referencing `math` while making other things only accesible by referencing it and it would look like this:
```py
import math
from math import sin

coolNumber: float = sin(math.pi)
```
This, however, can make code confusing by introducing inconsistancy so the best practice is not to do this.

### The "`as`" Keyword
When importing functions or variables from libraries, or even the entire library, we may not like the name they have given them. For example, if there was a package named `superAwesomeEpicMathCode` with the varibale `superAwesomeEpicMathSin`, the code would look like
```py
import superAwesomeEpicMathCode

coolNumber: float = superAwesomeEpicMathCode.superAwesomeEpicMathSin(3.14)
```
This is annoying to work with. Never fear, the '`as`' keyword can help solve this problem.

Lets take the theoretical named package and function, and use `as` to rename them. To rename the package
```py
import superAwesomeEpicMathCode as math

coolNumber: float = math.superAwesomeEpicMathSin(3.14)
```
As you can see, we renamed out package reference to be more managable. We can make this even better by renaming the reference to the function as well
```py
from superAwesomeEpicMathCode import superAwesomeEpicMathSin as sin

coolNumber: float = sin(3.14)
```
Say we wanted the variable `superAwesomeEpicMathPi` too, it would look like this:
```py
from superAwesomeEpicMathCode import superAwesomeEpicMathSin as sin, superAwesomeEpicMathPi as pi

```
Not fun to read at all so we can vertically seperate them to make it a little more managable
```py
from superAwesomeEpicMathCode import (
    superAwesomeEpicMathSin as sin,
    superAwesomeEpicMathPi as pi,
)

coolNumber: float = sin(pi) # works just fine
```

## Conclusion
That's pretty much all there is to it. In this tutorial, you learned:
* What an `import` statement is
* How they can be utilzed to share data between files
* How we can use it to access helpful tools from libraries

## Practice problems
