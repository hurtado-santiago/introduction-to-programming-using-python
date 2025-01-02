def count_words_starting_character(some_string, some_character):
    count=0
    list_words = some_string.lower().split()
    new_character = some_character.lower()
    for word in list_words:
        if word[0]==new_character:
            count += 1
    return count
    
input_string = 'chaolina shao lina'
character = 'c'
print(count_words_starting_character(input_string, character))
