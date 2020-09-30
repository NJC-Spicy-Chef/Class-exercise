# Statements using simple arithmetic integer.
# Page 41
x = 14
y = 8

result1 = x + y
result2 = x - y
result3 = x * y
result4 = x / y

results = (result1, result2, result3, result4)

print(results)

# Statements using simple arithmetic double
a = 8.5
b = 3.4

result1 = a + b
result2 = a - b
result3 = a * b
result4 = a / b

results = (result1, result2, result3, result4)

print(results)

# Page 43
a = 9
b = 4

result1 = a + b
result2 = a - b
result3 = a * b
result4 = a / b
result5 = a // b
result6 = a % b

results = (result1, result2, result3, result4, result5, result6)

print(results)
# Page 44 ??


# Python3 program two find number of
# days between two given dates

# A date has day 'd', month
# 'm' and year 'y'
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    # To store number of days in


# all months from January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]


# This function counts number of
# leap years before the given date
def countLeapYears(d):
    years = d.y

    # Check if the current year needs
    # to be considered for the count
    # of leap years or not
    if (d.m <= 2):
        years -= 1

    # An year is a leap year if it is a
    # multiple of 4, multiple of 400 and
    # not a multiple of 100.
    return int(years / 4 - years / 100 +
               years / 400)


# This function returns number of
# days between two given dates
def getDifference(dt1, dt2):
    # COUNT TOTAL NUMBER OF DAYS
    # BEFORE FIRST DATE 'dt1'

    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d

    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]

        # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += countLeapYears(dt1)

    # SIMILARLY, COUNT TOTAL NUMBER
    # OF DAYS BEFORE 'dt2'
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    # return difference between
    # two counts
    return (n2 - n1)


# Driver Code
dt1 = Date(1, 2, 2000)
dt2 = Date(1, 2, 2004)

print("Difference between two dates is",
      getDifference(dt1, dt2))

