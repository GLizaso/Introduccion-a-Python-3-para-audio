import math

a = input("Ingrese un numero mayor de 0:")
a = float(a)   # completar!
while a > 0: # completar!
    if a <=0:  # completar!
        print("Debe ingresar un numero positivo ")
        print("Este programa terminara")
        break
    print(["El logaritmo natural de " + str(a) + " es: " + str(math.log(a))])
    a = input("Ingrese un numero mayor de 0:")  # completar!
    a = float(a)  # completar!
print("Debe ingresar un numero positivo ")
print("Este programa terminara")