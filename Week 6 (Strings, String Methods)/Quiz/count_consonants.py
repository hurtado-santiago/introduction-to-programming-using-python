def count_consonants(some_string):
    new_string=some_string.lower().replace(' ', '')
    to_count='aeiou'
    count=0
    for letter in new_string:
        if letter not in to_count:
            count += 1
    return count
    
input_string = 'chaolin'
print(count_consonants(input_string))
