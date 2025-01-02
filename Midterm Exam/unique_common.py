def unique_common(a, b):
    output=[]
    for item_a in a:
        if item_a in b and item_a not in output:
            output.append(item_a)
    if not output:
        return None
    else:
        output.sort()
        return(output)

#a=[5, 6, -7, 8, 8, 9, 9, 10]
a=[5, 6, 7, 0]
#b=[2, 4, 8, 8, 5, -7]
b=[3, 2, 3, 2]
print(unique_common(a, b))
