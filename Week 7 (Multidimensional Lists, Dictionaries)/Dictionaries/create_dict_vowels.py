def create_dict_vowels(some_string):
    vowels="aeiou"
    new_string = some_string.replace(" ", "").lower()
    output={}

    for letter in new_string:
        if letter in vowels:
            output[letter] = new_string.count(letter)
    return output
                    
list_1 = "The cosmos is infinite"
print(create_dict_vowels(list_1))
