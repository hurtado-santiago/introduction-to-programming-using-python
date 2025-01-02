def vowels_count(some_string):
    new_string=some_string.upper()
    to_count='AEIOU'
    count=0
    for letter in to_count:
        count += new_string.count(letter)
    return count
    
input_string = 'chaolin'
print(vowels_count(input_string))
