def items_price(a, b):
    output=0
    for x in range(len(units)):
        output+=a[x]*b[x]
    return output


units = [2, 3, 5, 7, 9]
per_unit = [5, 8, 4, 1, 11]
print(items_price(units, per_unit))
