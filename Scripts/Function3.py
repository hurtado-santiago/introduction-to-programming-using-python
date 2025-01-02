# recibe una lista de enteros y los promedia, devolviendo el resultado a traves de una funcion
def process (x):
    y = 0
    size = len (x)
    for z in x:
        y = y + z
    y = y/size
    return y

list = [0, 1, 2, 3, 4]
add = process (list)
print (add)
