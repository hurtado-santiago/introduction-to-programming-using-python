def chasing_cases(some_string):
    new_string=""
    for letter in some_string:
        if (ord(letter)<= 90) and (ord(letter)>=65):
            x=chr(ord(letter)+32)
            new_string+=x
        elif (ord(letter)<= 122) and (ord(letter)>=97):
            x=chr(ord(letter)-32)
            new_string+=x
        else:
            new_string+=letter
    return new_string

input_string = "Hello"
print(chasing_cases(input_string))
