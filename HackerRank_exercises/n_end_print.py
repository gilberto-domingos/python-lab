""" Without using string methods, print:
    All numbers from 1 to n, without spaces and on the same line :
"""
print("Enter a number :")
n = int(input())
for i in range(1, n + 1):
    print(i, end="")
