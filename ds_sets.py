import sys

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
empty_variable = None
print(type(empty_variable))
print(id(empty_variable))
print(sys.getsizeof(empty_variable))

# Binary - bytes, bytearray, memoryview
byte_structure = bytes.fromhex('2Ef0 F1f2  ')
print(byte_structure)
byte_array_structure = bytearray.fromhex('2Ef0 F1f2  ')
print(byte_array_structure)

# Bytes
print(b'This is binary text')

# Bytearray
print(bytearray(b'\xf0\xb1\xc2').hex())

# Memoryview
test = memoryview(b'Acidophilus')
print(test[1])


# Boolean
an_identifier = False
print(type(an_identifier))
print(id(an_identifier))
print(sys.getsizeof(an_identifier))

# Integer, Float, Complex
int_identifier = 17
float_identifier = 9.8
complex_identifier = 14 +3j

# String
string_identifier = "This is a line of text."
multiline_string_identifier = '''Two lines
of text'''


# Sets
fictional_characters = {"Rick Sanchez", "Morty Smith", "Beth Smith", "Jerry Smith", "Summer Smith"}
print(len(fictional_characters))
print(id(fictional_characters))
print(sys.getsizeof(fictional_characters))

# FrozenSet
frozen_fictional_characters = frozenset(fictional_characters)
print(frozen_fictional_characters)
print(sys.getsizeof(frozen_fictional_characters))

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
print(column_major_matrix[2][0])

'''
Stacks
'''

class DataStructure:
    test_variable = 99

class Stack(DataStructure):
    random_property = "test"
    x = []

    def __init__(self):
        self.x = []

    def push(self, element):
        self.x.append(element)

    def pop(self):
        element = self.x.pop()
        return element

object = Stack()
print(object.x)
object.push(12)
object.push(56)
print(object.x)
object.pop()


'''
Linked Lists
'''


class Node:
    data_value = None
    next_value = None

    def __init__(self, new_value):
        self.data_value = new_value

    def append(self, new_value):
        new_node = Node(new_value)
        self.next_value = new_node

'''
class LinkedList:
    first_node = None

    def __init__(self):
        self.first_node(
'''  
        

test_node = Node(27)
print(test_node.data_value)
test_node.append(73)
print(test_node.next_value.data_value)
print(type(test_node).__mro__)


'''
Hash Tables
'''

# Dictionary
score_dictionary = {'megan': 89, 'jake': 55, 'sue':77, 'mike': 99, 'orwell':91}
print(score_dictionary)
print(score_dictionary['orwell'])
