

import random

numero_secreto = random.randint(1, 24)

print("Tienes 3 intentos para adivinar el numero secreto entre 1 y 24.")

intentos_restantes = 3

while intentos_restantes > 0:
    intento = int(input("Ingrese un numero: "))

    if intento == numero_secreto:
        print("Has adivinado el numero secreto.")

    else:
        intentos_restantes -= 1
        if intento < numero_secreto:
            print("El nuemero es mayor que", intento)
        else:
            print("El numero es menor que", intento)

        if intentos_restantes > 0:
            print("Te quedan", intentos_restantes, "intento.")
        else:
            print("Has agotado tu numero de intentos. El numero secreto es", numero_secreto)

