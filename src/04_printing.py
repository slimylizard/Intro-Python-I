"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x : %2d, y : %3.2f, z : %s" %(10, 2.25, z))
# Use the 'format' string method to print the same thing
txt = "x : {int:2d}, y : {float:3.2f}, z : {ss:s}"
print(txt.format(int = 10, float = 2.25, ss = "I like turtles!"))
# Finally, print the same thing using an f-string
F"x {x}, y {y}, z {z}"