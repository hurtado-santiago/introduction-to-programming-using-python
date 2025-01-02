def count_input_character(some_string, some_character):
    count=0
    new_string = some_string.lower()
    new_character = some_character.lower()
    for letter in new_string:
        if new_character == letter:
            count += 1
    return count
    
input_string = 'chaolina'
character = 'a'
print(count_input_character(input_string, character))
