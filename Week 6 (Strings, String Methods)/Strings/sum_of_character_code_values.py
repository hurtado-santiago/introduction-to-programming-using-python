def sum_of_character_code_values(word):
    add=0
    for letter in word:
        add+=ord(letter)
    return add

word = 'hello'
print(sum_of_character_code_values(word))
