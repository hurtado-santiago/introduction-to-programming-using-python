def find_longest_word(some_string):
    some_list=some_string.split()
    count = 0
    for index, word in enumerate(some_list):
        if len(word) >= count:
            count = len(word)
            long_word=some_list[index]
    return long_word
    
input_string = 'chaolin popeye raul francisco'
print(find_longest_word(input_string))
