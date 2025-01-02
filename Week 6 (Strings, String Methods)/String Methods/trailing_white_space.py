def trailing_white_space(some_string):
    for x in range(len(some_string)-1, 0, -1):
        if some_string[x] != " ":
            indice = some_string.find(some_string[x])
            break
        
    new_string=some_string[:indice+1]
    return new_string

input_string = "  Hello       "
print(trailing_white_space(input_string))
