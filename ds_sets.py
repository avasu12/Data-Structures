# Sets

# Sets can be dynamic - grow, shrink, change
# Sets are immutable, and contain no duplicates

random_set = {0, 1, 1, 2, 3, 5, 8}

print(random_set)

''' 
Categories of operations on sets: 
1. Queries
2. Modifications
'''

print(len(random_set))
another_set = set((1, "five", False, 365, 0))
print(another_set)
print(len(another_set))
another_set.pop()
print(another_set)
another_set.add(3.14)
print(another_set)