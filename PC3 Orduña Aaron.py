# solucion1
print("Solucion 1")

def long_ult_palabra(frase):
    if len(frase) == 0:
        return 0
    cantidad=0
    for i in range(len(frase)):
        if frase[i]!=' ':
            cantidad+=1
        else:
            if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
    return cantidad    
frase = input("Ingrese una frase: ")
result = long_ult_palabra(frase)
print(result)


# solucion2
print("Solucion 2")
def capitprimlet(frase):
    resultado = ""
    for palabra in frase.split():
        resultado += palabra[0].upper() + palabra[1::] + " "
    return resultado

frase = input("Ingrese una frase: ")
print(capitprimlet(frase))


# solucion3
print("Solucion 3")
from math import pi   
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
area1 = CIRCULO(int(input("ingrese un valor de radio: ")))
area1.radio
def area(pi, r):
    return pi * area1.radio * area1.radio
print(f"Area: {(pi, area1.radio)}")


# solucion4
print("Solucion 4")          
class rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
area2 = rectangulo(int(input("ingrese un valor de largo: ")), int(input("ingrese un valor de ancho: ")))
def area(l, a):
    return area2.largo * area2.ancho
print(f"Area: {area(area2.largo, area2.ancho)}")


# solucion5
print("Solucion 5") 
class Alumno:
    def __init__(self, display, setage, setnota):
        self.display = display
        self.setage = setage
        self.setnota = setnota
est = Alumno(input("Ingresar nombre y número de registro de estudiante: "), int(input("Ingresar edad del estudiante: ")), int(input("Ingresar notas del estudiante: ")))
print(est.display)
print(est.setage)
print(est.setnota)




# solucion6
try:
    li=[]
    for x in range(6):
        valor = li.append(int(input("Ingrese una nota:")))         
    print(li)
except:
    print("Ingrese correctamente el valor")



# solucion7
print("Solucion 7")
def triangpascal(filas):
    fila = [1]
    cero = [0]

    for i in range(filas):
        print(fila)

        fila = [i + d for i, d in zip(fila + cero, cero + fila)]

triangpascal(int(input("Ingrese el numero de fila: ")))



# solucion8
print("Solucion 8")
print("Ir a directorio problema8")



# solucion9
print("Solucion 9")
print("Ir a directorio problema9")


# solucion10
print("Solucion 10")
print("Ir a directorio problema10")



