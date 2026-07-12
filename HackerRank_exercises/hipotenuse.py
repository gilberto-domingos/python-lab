"""Point M is the midpoint of the hypotenuse AC.
The following lengths are given: AB , BC
Your task is to find the angle MBC (the angle at B formed by segments BM and BC) in degrees.
"""
import math
print("Enter two numbers :")
AB = int(input())
BC = int(input())

angle = round(math.degrees(math.atan(AB / BC)))

print(f" Angle is : {str(angle)}°")