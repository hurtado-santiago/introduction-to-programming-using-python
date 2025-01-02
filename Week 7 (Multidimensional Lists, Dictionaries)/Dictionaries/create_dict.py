def create_dict(some_string):
    new_string = some_string.replace(" ", "").lower()
    output={}

    for letter in new_string:
        output[letter] = new_string.count(letter)
    return output
                    
list_1 = "The cosmos is infinite"
print(create_dict(list_1))
