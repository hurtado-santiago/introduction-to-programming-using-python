def reversed_case_swapped(some_string):
    count_letter=0
    max_count=0
    new_string = some_string.swapcase()[::-1]
    return new_string
    

input_string = 'Hello Python World'
print(reversed_case_swapped(input_string))
