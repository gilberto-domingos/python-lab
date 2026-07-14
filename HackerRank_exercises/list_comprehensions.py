"""You are given three integers x, y, and z, representing the dimensions of a cuboid, along with an integer n.
You must print a list containing all possible coordinates [i, j, k] of a 3D grid, where:
0 <= i <= x
0 <= j <= y
0 <= k <= z

However, there is a condition:
The sum i + j + k cannot be equal to n.
The goal of the exercise is to use list comprehension instead of multiple for loops."""
print("Enter 4 numbers :")
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

print(result)
