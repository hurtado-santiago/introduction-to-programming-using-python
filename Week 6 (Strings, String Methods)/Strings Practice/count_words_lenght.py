def count_words_lenght(some_string):
    lenght=4
    count=0
    list_words = some_string.lower().split()
    for word in list_words:
        if len(word)>lenght:
            count += 1
    return count
    
input_string = 'chaolina shao lina'
print(count_words_lenght(input_string))
