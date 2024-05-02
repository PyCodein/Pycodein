


a = float(input("Ingrese un numero real: "))
operador = input("Ingrese operador(+, -, *, /): ")
b = float(input("Ingrese un numero real: "))

while operador == "/" and b == 0:
    print("Error, no se puede dividir por 0. Vuelva a ingresar un numero.")
    b = float(input("Ingrese de nuevo el segundo numero real: "))

if operador == "+":
    resultado = a + b

elif operador == "-":
    resultado = a - b

elif operador == "*":
    resultado = a * b

elif operador == "/":
    resultado = a / b

else:
    print("Operador no valido")

print(resultado)
