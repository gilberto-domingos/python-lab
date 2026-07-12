""" Gregorian calendar rules
A year is a leap year if:
It is divisible by 4, except when:
It is divisible by 100, in which case it is not a leap year, except when:
It is also divisible by 400, in which case it is a leap year.
  Given a year, determine if it is a leap year:
"""

print("Enter a year :")
year = int(input())


def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


if is_leap(year):
    print(f"Year {year} is leap")
else:
    print(f"Year {year} is not leap")
