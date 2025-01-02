# recibe una lista de enteros y devuelve el mayor de ellos a traves de una funcion
def process (x):
    y = x[0]
    for z in x:
        if z > y:
            y = z
    return y

list = [0, 5, 2, 3, 4]
add = process (list)
print (add)
