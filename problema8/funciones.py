import random
def lista_num():
    listan=[]
    for x in range(20):
        listan.insert(x, random.randrange(0,100))
    return listan
listan = lista_num()

def imprimir(listan):
    print(listan)

def ordenar():
    return sorted(listan)
orden = ordenar()

