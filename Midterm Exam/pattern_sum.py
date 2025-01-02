def pattern_sum(a, b):
    output=0
    actual = ''
    for x in range(b):
        actual += str(a)
        output += int(actual)
    return(output)

a,b=4, 5
print(pattern_sum(a, b))
