def num_to_word(some_string):
    new_string = str(some_string)
    output = ""
    numbers={'0':'zero',
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine'}

    for number in new_string:
        output += numbers[number]+" "
    return output.strip()
                  
number = 5124
print(num_to_word(number))
