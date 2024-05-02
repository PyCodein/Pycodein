
peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))

imc = peso / (altura ** 2)

if edad < 45:
    if imc < 22:
        riesgo = 1
    else:
        riesgo = 2
else:
    if imc < 22:
        riesgo = 2
    else:
        riesgo = 3

print("El nivel de riesgo es:", riesgo)