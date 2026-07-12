"""You are given a positive integer n.
Print a numeric triangle with height n, like the example below:
1
22
333
4444
55555
......
"""
print("Enter a number :")
n = int(input())

for i in range(1, n):
    print(((10 ** i - 1) // 9) * i)
