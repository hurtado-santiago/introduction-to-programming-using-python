def preserve_reverse(some_string):
    some_list=some_string.split(' ')
    for x in range(len(some_list)):
        some_list[x]=some_list[x][::-1]
    new_string = ' '.join(some_list)
    return new_string
    

input_string = 'this is a sample test'
print(preserve_reverse(input_string))
