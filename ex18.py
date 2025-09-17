#A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.

#Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.

#Write a code find if a given year is a leap year.

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


user_input = int(input("year to check: "))
print(is_leap(user_input))


# or make it with nested ifs
# if year % 4 == 0:
#   if year % 100 == 0:
#       if year % 400 == 0:

