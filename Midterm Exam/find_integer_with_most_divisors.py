def find_integer_with_most_divisors (input_list):
    most = 0
    value = 0
    for x in input_list:
        div = 0
        for y in range(1, x+1):
            if x%y == 0:
                div = div + 1
        if most<div:
            most = div
            value = x
    return(value)


values = [8, 12, 18, 6]
print(find_integer_with_most_divisors(values))
