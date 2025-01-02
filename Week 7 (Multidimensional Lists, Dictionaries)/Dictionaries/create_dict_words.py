def create_dict_words(some_string):
    new_string = some_string.lower().split(" ")
    output={}

    for word in new_string:
        output[word] = new_string.count(word)
    return output
                    
list_1 = "I am tall when I am young and I am short when I am old" 
print(create_dict_words(list_1))
