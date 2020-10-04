# ExerciseGiven the year of manufacture of a car,
# write a program to calculate how many years have
# elapsed since production. Print the results in a nice format.1.Calculate the number of months elapsed since production.
# How about the number of days?'''

import datetime

now = datetime.datetime.now().year
year = input("What is the year of manufacture: ")
elapsedYears = int(now) - int(year)
elapsedMonths = elapsedYears * 12
elapsedDays = elapsedYears * 365.12

result1 = elapsedYears
result2 = elapsedMonths
result3 = elapsedDays

print("The time elapsed since manufacture are ",result1, "years ", "/", result2, "months ", "/", result3, "days. ")
