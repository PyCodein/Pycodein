

#Escriba un programa en Python que permita desarrollar la Serie de Leibniz hasta el término n y que muestre el valor de pi obtenido 
#(recuerde que, para elevar un número, se usa “ ** ”).


a = int(input("Ingrese el número de términos para la Serie de Leibniz: "))

pi_approximation = 0
for i in range(a):
    pi_approximation += (-1) ** i / (2 * i + 1)

pi_value = pi_approximation * 4

print("El valor aproximado de pi usando la Serie de Leibniz con", a, "términos es:", pi_value)
