# recibe una lista de enteros y los suma, devolviendo el resultado a traves de una funcion
def process (x):
    y = 0
    for z in x:
        y = y + z
    return y

list = [0, 1, 2, 3, 4]
add = process (list)
print (add)
