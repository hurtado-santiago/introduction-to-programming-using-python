def sorted_test(some_list):
    sorted_list=sorted(some_list)
    if sorted_list == some_list:
        return True
    else:
        return False

input_list = ['chao', 'hola']
print(sorted_test(input_list))
