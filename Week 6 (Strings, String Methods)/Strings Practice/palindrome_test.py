def palindrome_test(some_string):
    new_string=some_string.strip().lower()
    reverse_string=new_string[::-1]
    if new_string == reverse_string:
        return True
    else:
        return False

input_string = "Alo"
print(palindrome_test(input_string))
