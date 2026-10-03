# For Loops

## *Goal: Utilize a for loop to complete a repetitive task efficiently*

## *Prerequisites: Variables, Conditionals, Functions*

Some processes in code can be very repetitive and as such, loops become a better way to do things because they are easier to both read and write. The foundational loop is the While loop. It works by repeating the code inside of it while a Condition is True. Imagine a car updating and displaying its backup camera while the car is in reverse.

Syntax:

```py
while True:
	print("Hello World")
```

This specific while loop would in fact loop forever because, well, True is always True

While loops are nice but if you wanted to repeat something 10 times, you can’t really write a conditional statement in a while loop to track that so we use something called a For Loop. (Actually, a for loop is secretly a while loop that tracks the amount of times it loops, and still uses a conditional so that's a lie)

For Loop Syntax:

```py
for i in range(10):
print("Hello World")
```

This particular for loop would repeat `10` times (the number in the `“range()”` function) but there is something even more useful about a for loop and that the little `“i”` variable. 

This is commonly named the “index” or "iterator" hence why it’s an `“i”`. Both of these terms essentially describe that our variable is meant to track where we are in the loop, and that’s exactly what it does. How it works is that our variable will increase by 1 every time the loop passes, or "iterates," through and reaches the end of the code.

```py
for i in range(10):
print(i)
```

In this basic format, `“i”` will start at zero and increase by 1 until it reaches `10`. You may notice if you run this code that 10 is actually never printed and the reason for this is because every time our loop goes back up to the top, it checks if `“i”` is less than `10` and then decides to run the code again or not. In our case, when `“i”` is equal to 9 and it reaches the end of the code, it will increase by 1 to 10\. Then, the loop will evaluate if 10 is less than `10`, and since it isn’t the loop will stop, or “break,” and the rest of the program will continue on.

There are also other forms of the `“range()”` function we can use.

```py
for i in range(1, 10):
pass
```

This is the `range(start, stop)` structure. Start is what `“i”` will start at.

```py
for i in range(1, 10, 2):
	pass
```

This is the `range(start, stop, step)` structure. Step is what `“i”` will increase by every iteration.

```py
for i in range(10, 1, -1):
	pass
```

Step can also be negative but this changes the loop to check if `“i”` is greater than stop at the top of the loop so something like this:

```py
for i in range(1, 10, -1):
	pass
```

Would never run because `1` is immediately less than `10`

Here’s a fun little program that utilizes a for loop to sing a very repetitive song

```py
for i in range(99, 0, -1):
    print(i, "bottles of beer on the wall")
  print(i, "bottles of beer")
  print("take 1 down, pass it around,")
    print(i-1, "bottles of beer on the wall.")

```

Notice the `i-1` to cheekily get the next number down

# Challenge

I want to know all the odd numbers in the range 0 to 101 (inclusive\!). Utilize a loop to `print(`) all the odd numbers in the range in order.

As a bonus, think of something repetitive you can achieve in code with a for loop  
