'''

Data Structures

Physical implementation (organization) of various types of data
They can be point structures (small/smallest addressable units of data) or sets (a collection of data points)

'''


'''

Point structures:
Primitive types
Composite types
Abstract types

'''

# None

# Binary

# Boolean

# Integer, Float, Complex

# String



'''
Set structures

# Sets can be dynamic - grow, shrink, change
# Sets are immutable, and contain no duplicates

'''

''' 
Categories of operations on sets: 
1. Queries
2. Modifications
'''

'''
Arrays
'''

# Sets can't be arrays because they aren't ordered/indexable? Or stored contiguously in memory?
list_array = ["Zara", "H&M", "Zodiac"]
tuple_array = (True, False, True, True)

print(list_array[2])

'''
Matrices
'''

# Two dimensional arrays
row_major_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

column_major_matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(row_major_matrix[1][2])
print(column_major_matrix[2][0]
