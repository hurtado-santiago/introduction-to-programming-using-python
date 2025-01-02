def find_word_horizontal(some_list, some_string):
    if not some_list or not word:
        return None

    for index, row in enumerate(some_list):
        new_string=''.join(row)
        if new_string.find(some_string) >= 0:
            return [index, new_string.find(word)]
    return None    
                  
crosswords = [['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word = 'cat'
print(find_word_horizontal(crosswords, word))
