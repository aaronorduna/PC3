
def suma():
    try:
        a = float(input("Ingrese un numero: "))
        b = float(input("Ingrese un numero: "))
        print(f"{a} + {b} = {a + b}")
    except:
        print("Error: tipo de dato inválido")
suma()


def resta():
    try:
        a = float(input("Ingrese un numero: "))
        b = float(input("Ingrese un numero: "))
        print(f"{a} - {b} = {a - b}")
    except:
        print("Error: tipo de dato inválido")
resta()


def producto():
    try:
        a = float(input("Ingrese un numero: "))
        b = float(input("Ingrese un numero: "))
        print(f"{a} * {b} = {a * b}")
    except:
        print("Error: tipo de dato inválido")
producto()


def division():
    while(True):
        try:
            a = float(input("Ingrese un numero: "))
            b = float(input("Ingrese un numero: "))
            if b == 0:
                print("Error: No es posible dividir entre cero")
            print(f"{a}/{b} = {a / b}")
        except:
            print("Error: tipo de dato inválido")
        else:
            break
division()




    

