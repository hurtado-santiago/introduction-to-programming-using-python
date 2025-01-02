def find_word_vertical(some_list, some_string):    
    if not some_list or not word:
        return None

    len_col=len(some_list[0])

    for index in range(len_col):
        new_string=''
        for row in some_list:
            new_string+=row[index]
        if new_string.find(some_string) >= 0:
            return [new_string.find(word), index]
    return None    
                  
crosswords = [['s','d','o','g'],
              ['c','u','c','m'],
              ['a','c','a','t'],
              ['t','e','t','k']]
word = 'cat'
print(find_word_vertical(crosswords, word))
