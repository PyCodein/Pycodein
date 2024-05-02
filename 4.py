

a = int(input())
b = int(input())
c = int(input())

par = 0
impar = 0

if a % 2 == 0:
    par += 1
else:
    impar += 1

if b % 2 == 0:
    par += 1
else:
    impar += 1

if c % 2 == 0:
    par += 1
else:
    impar += 1

if par == 2 or impar == 2:
    print("Variadito")
else:
    print("Uniforme")