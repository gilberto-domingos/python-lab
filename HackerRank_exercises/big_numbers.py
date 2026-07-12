""" Integers in Python can be as large as the machine's available memory allows. Unlike languages as C++:
Read four numbers: a, b, c, d
Print the result of:
a ** b + c ** d
"""
print("Entar 4 numbers :")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# print(a ** b + c ** d)
first_power = a ** b
second_power = c ** d

result = first_power + second_power

print(result)
