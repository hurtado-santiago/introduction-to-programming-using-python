def list_to_tuples(some_list):
    for in_list in some_list:
        in_list=in_list.reverse()
    for index in range (0, len(some_list)):
        some_list[index]=tuple(some_list[index])
    return(tuple(some_list))


input_list=[['mean', 'really', 'is', 'jean'], ['world', 'my', 'rocks', 'python']]
print(list_to_tuples(input_list))
