# recibe una vector de 3 componentes y devuelve la magnitud de este
def process (x):
    magnitude = 0
    for z in x:
            magnitude = magnitude + z*z
    magnitude = magnitude**(1/2)
    return magnitude

vector = [2, 3, -4]
out = process (vector)
print (out)
