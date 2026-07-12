# This exercise takes an integer n and applies the following rules:
# If n is odd → "Weird"
# If n is even and between 2 and 5 → "Not Weird"
# If n is even and between 6 and 20 → "Weird"
# If n is even and greater than 20 → "Not Weird"


print("Enter a number : ")
n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
