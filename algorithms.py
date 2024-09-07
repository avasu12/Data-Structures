'''
Insertion sort
'''

# Input list

# test_list = [34,20,77,91,27,8,42]
unsorted_list = input("Please enter a list of integers, separated by commas")
unsorted_list = unsorted_list.split(',')

for digit in unsorted_list:
    digit = int(digit)

# print(test_list)

for insert_index in range(1, len(unsorted_list)):
    insert_number = unsorted_list[insert_index]
    check_index = insert_index - 1
    while insert_number > unsorted_list[check_index]:
        check_index -= 1

        