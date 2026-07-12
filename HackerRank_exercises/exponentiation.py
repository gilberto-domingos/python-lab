"""Powers (exponents) in Python can be calculated using the built-in `pow()` function.
`a` and `b` can be negative numbers or decimals.
However, when a third argument (`m`) is present, the exponent `b` cannot be negative.
There is also `math.pow()`, but it returns a float and is rarely used in this context.
You will receive three integers: a, b, m
You must print:
The result of `pow(a, b)`
The result of `pow(a, b, m)`
"""
print("Enter 3 numbers :")
a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))
