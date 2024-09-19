


# An assert statement

variable_one = "string"
variable_two = 'string'


assert variable_one == variable_two

integer_var = 17
float_var = 18.0

assert integer_var < float_var, "Assertion message"


# The pass keyword

def calculate_distance(point_a: int = 17, point_b: int = 9) -> int:
    pass
    pass
    pass
    pass

pass
pass

# del statement

x = 10
del x
my_list = ["avocado", "potato", "leek", "lettuce"]
del my_list[1]
print(my_list)

# The global statement
y = 15
def write_message():
    global y
    y = 20
    print(y)

write_message()
print(y)


# The with statement

with open('algorithms.py', 'r') as file:
    # print(file.read())
    print(file.__enter__())
    print(file.__exit__)
    file.close()
    file.close()

# The type statement

type Coordinate = tuple[float, float]
print(Coordinate)

# The yield statement

def count_stuff():
    count = 5
    while count > 0:
        yield count
        count-=1

yield_response = count_stuff()
print(yield_response)