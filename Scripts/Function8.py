# recibe una vector de 3 componentes y devuelve los vectores unitarios
def process (lista):
    magnitude = 0
    normalize = 0
    for item in lista:
            magnitude = magnitude + item*item
    magnitude = magnitude**(1/2)
    x = lista[0]/magnitude
    y = lista[1]/magnitude
    z = lista[2]/magnitude
    return [x,y,z]

vector = [2, 3, -4]
out = process (vector)
print (out)
