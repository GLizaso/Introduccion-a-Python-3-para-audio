#Ejercio de archivo Primeros pasos con Python
#Clase 2


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b;


num1 = input("Num1: ")
num2 = input("Num2: ")

print("Opciones\n1.- Sumar\n2.- Restar\n3.- Multiplicar")

operaciones = {'1': sumar, #Para que funciones el diccionario el key tiene que estar entre comillas simples.
               '2': restar,
               '3': multiplicar}  # completar!

seleccion = input('Escoge una: ')

try:
    resultado = operaciones[seleccion](int(num1), int(num2))  # completar!
    print(resultado)
except:

    print("Esa no vale")