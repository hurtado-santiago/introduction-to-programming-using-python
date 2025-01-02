def process (height, width):
    area = height * width
    perimeter = (height + width)*2
    result = [area, perimeter]
    return (result)

solve = process (4, 2)
print (solve)
