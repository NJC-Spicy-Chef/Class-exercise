# Multidimensional Lists
# Exercise 6

my_list = ["A", "B", "C"]

# 1. Create a new list "copied_list_1" by copying the list by assignment (a=b).
copied_list_1 = my_list
print("1.", copied_list_1)

# 2. Create a new list "copied_list_2" by copying the list with the deep copy operator (x.copy) or the (":") operator.
copied_list_2 = my_list[:]
print("2a.", copied_list_2)

copied_list_2 = my_list.copy()
print("2b.", copied_list_2)

# 3. In the original my_list, change "B" to "X".
my_list[1] = "X"
print("3.", my_list)

# 4. Display both lists using the "print" command.
print("4.", my_list, copied_list_1, copied_list_2)



