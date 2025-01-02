def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    new_string = ""
    
    for letter in some_string:
        index = character_set.find(letter)
        new_string += secret_key[index]
    return new_string
    
first_string = "Lets meet at the usual place at 9 am"
print(my_encryption(first_string))
