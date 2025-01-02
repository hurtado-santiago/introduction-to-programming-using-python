def n_letter_dictionary(some_string):
    some_dict={}
    output={}
    new_string=some_string.strip().split(" ")
    for word in new_string:
        word=word.lower()
        if some_dict.get(len(word)):
            if word not in some_dict[len(word)]:
                some_dict[len(word)].append(word)
                some_dict[len(word)].sort()
        else:
            some_dict[len(word)]=[word]
        
    keys=some_dict.keys()
    keys=sorted(keys)
    for key in keys:
        output[key]=some_dict[key]
    return(output)


some_input = "The way you see people is the way you treat them and the Way you treat them is what they become"
print(n_letter_dictionary(some_input))
