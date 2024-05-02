

total = int(input())

if 5000 <= total <= 10000:
    des = total * 0.9
    print("Se aplico un descuento del 10%")
elif 10001 <= total <= 20000:
    des = total * 0.8
    print("Se aplico un descuento del 20%")
else:
    des = total

print(des)