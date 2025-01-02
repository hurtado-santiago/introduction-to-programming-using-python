def find_word_horizontal(some_list, some_string):
    for index, row in enumerate(some_list):
        new_string=''.join(row)
        if new_string.find(some_string) >= 0:
            return [index, new_string.find(word)]
    return None

                  
def find_word_vertical(some_list, some_string):
    len_col=len(some_list[0])

    for index in range(len_col):
        new_string=''
        for row in some_list:
            new_string+=row[index]
        if new_string.find(some_string) >= 0:
            return [new_string.find(word), index]
    return None


def capitalize_word_in_crossword(some_list, some_string):
    if not some_list or not word:
        return None

    len_word=len(word)
    
    location=find_word_horizontal(some_list, some_string)
    if location:
        for index in range(location[1], location[1]+len_word):
            some_list[location[0]][index]=str(some_list[location[0]][index]).upper()
        return some_list

    if location == None:
        location=find_word_vertical(some_list, some_string)
        for index in range(location[0], location[0]+len_word):
            some_list[index][location[1]]=str(some_list[index][location[1]]).upper()
        return some_list

    return location

crosswords = [['s','d','o','g'],
              ['c','u','c','m'],
              ['a','c','a','t'],
              ['t','e','t','k']]
word = 'cat'
print(capitalize_word_in_crossword(crosswords, word))
