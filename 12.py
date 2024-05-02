

#Construya un programa que lea el valor de un número entero y que lo despliegue sólo si el valor es mayor que cero. 
#Mientras no se ingrese un valor positivo el algoritmo debe generar el mensaje “Error, valor mal ingresado” y pedir otro número.

while True:

    a = int(input())

    if a > 0:
        print(a)
        break
    else:
        print("Error, valor mal ingresado. Ingrese otra vez.")