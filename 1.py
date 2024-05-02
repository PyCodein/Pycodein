

while True:

    a = int(input())
    b = int(input())

    if a < b:
        print(a * 2)
        break
    elif a == b:
        print("Error, ingrese otra vez: ")
    else:
        print(b * 2)
        break