def most_common_character(some_string):
    count_letter=0
    max_count=0
    new_string = some_string.lower().replace(' ', '')
    
    for letter in new_string:
        count_letter=new_string.count(letter)
                
        if count_letter>=max_count:
            max_count=count_letter
            char = letter
            
    return char
    

input_string = 'Hello Python World'
print(preserve_reverse(input_string))
