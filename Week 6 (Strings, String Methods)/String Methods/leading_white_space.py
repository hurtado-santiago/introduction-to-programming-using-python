def leading_white_space(some_string):
    for letter in some_string:
        if letter != " ":
            indice = some_string.find(letter)
            break
        
    new_string=some_string[indice::]
    return new_string

input_string = "    Hello  "
print(leading_white_space(input_string))
