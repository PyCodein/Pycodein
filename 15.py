

a = int(input("Ingrese un numero: "))

print("Tabla de multiplicar del", a, ":")

for i in range(1, 11):
    resultado = a * i
    print(a, "x", i, "=", resultado)