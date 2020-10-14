# Page 17 Exercise 5
# 1. Create a new list with the first ten values of 2n
# 2. Use the "pow" (power) function for this.

# pow(value, exponent) calculate the first power of 2 to the 10.

new_list = []
for i in range(11):
    new_list.append(pow(2, i))
print(new_list)

# This is more efficient code
new_list1 = [pow(2, i) for i in range(11)]
print(new_list1)
