def remove_all_spaces(some_string):
    new_string=""
    for letter in some_string:
        if ord(letter)!= 32:
            new_string+=letter
            
    return new_string

input_string = " Hel lo "
print(remove_all_spaces(input_string))
