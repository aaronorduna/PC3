import random
def cargar():
    return int(input("Ingresa un numero entero: "))

def aleatorio():
    return random.randrange(1,100)
  
def adivinar():
    num = aleatorio()
    print("Bienvenido al juego 'Adivina el numero'")
    correcto=False
    while correcto == False:
        n = cargar()
        if num ==n:
            print("Has ganado")
        elif num<n:
            print("El numero aleatorio es menor, ingresar otro numero")
        else:
            print("El numero aleatorio es mayor, ingresar otro numero")

