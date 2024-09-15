


# An assert statement

variable_one = "string"
variable_two = 'string'


assert variable_one == variable_two


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
