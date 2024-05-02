


a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c


if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

medio = (a + b + c) - (mayor + menor)

print(mayor, medio, menor)