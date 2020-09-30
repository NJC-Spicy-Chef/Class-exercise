import random
import antigravity
# Page 12 Exercise 2 (20 min.)
# 1. Create a list of 20 numbers, randomly assigned.
# 2. To generate the list, we can use:
# 3. random_list= [random.randrange(1, 100) for i in range(20)]
# 4. Scan the list and display several values using a manual method:
# 5. The minimum, the maximum, the count and the average.

number_list = [random.randrange(1, 100) for i in range(20)]
# for i in range(1, 21):
#    j = random.randint(1, 100)
#    number_list.append(j)
print(number_list)
print('Minimum:', min(number_list))
print('Maximum:', max(number_list))
print('Count:', len(number_list))
print('Average:', sum(number_list)/len(number_list))

print("\n")

# Exercise 4
'''
my_list = ['A', 'B', 1, 2, 3]
print(my_list)
print('Minimum:', min(my_list))
print('Maximum:', max(my_list))
print('Count:', len(my_list))
print('Average:', sum(my_list)/len(my_list))

'''
# Page 17 Exercise 5
# 1. Create a new list with the first ten values of 2n
# 2. Use the "pow" (power) function for this.

# pow(value, exponent) calculate the first power of 2 to the 10.

new_list = []
for i in range(11):
    new_list.append(pow(2,i))
print(new_list)

# This is more efficient code
new_list1 = [pow(2, i) for i in range(11)]
print(new_list1)

print("\n")
# Multidimensional Lists

# Exercise 6
# Given an input list:
# mylist= ["A", "B", "C"]

mylist = ["A", "B", "C"]

# 1. Create a new list "copied_list_1" by copying the list by assignment (a=b).
copied_list_1 = mylist
print("1.", copied_list_1)

# 2. Create a new list "copied_list_2" by copying the list with the deep copy operator (x.copy) or the (":") operator.
copied_list_2 = mylist[:]
print("2a.", copied_list_2)

copied_list_2 = mylist.copy()
print("2b.", copied_list_2)

# 3. In the original my_list, change "B" to "X".
mylist[1] = "X"
print("3.", mylist)

# 4. Display both lists using the "print" command.
print("4.", mylist, copied_list_1, copied_list_2)














