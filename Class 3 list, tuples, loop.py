import random

# Lists
# Page 33 Exercise 1 (5 min)
from random import random

mylist2 = ['red', 'green', 'blue']
print('0. ', mylist2)

# 1. Add two colours to the end, 'black' and 'white'.
mylist3 = ['black', 'white']
mylist2.extend(mylist3)
print('1. ', mylist2)

# 2. Change the third item to 'yellow'.
mylist2[2] = 'yellow'
print('2. ', mylist2)

# 3. Delete the colour green by position.
del mylist2[1]
print('3. ', mylist2)

# 4. Delete the colour red by name.
mylist2.remove('red')
print('4. ', mylist2)

print("\n")

# 5. Make a for loop to print each remaining item, capitalized, with a line number in front of it.
for color in mylist2:
    colorIndex = mylist2.index(color) + 1
    firstUpperCase = color[0].upper() + color[1:]
    print(colorIndex, firstUpperCase)

