import random
# Page 12 Exercise 2 (20 min.)
# 1. Create a list of 20 numbers, randomly assigned.
# 2. To generate the list, we can use:
# 3. random_list= [random.randrange(1, 100) for i in range(20)]
# 4. Scan the list and display several values using a manual method:
# 5. The minimum, the maximum, the count and the average.

number_list = [random.randrange(1, 100) for i in range(20)]

print(number_list)
print('Minimum:', min(number_list))
print('Maximum:', max(number_list))
print('Count:', len(number_list))
print('Average:', sum(number_list)/len(number_list))


