x = int(input("Ingrese su valor de X "))

if x <= 0 and x >= 10:
    fx = 5 * x + 12 
    print(f"el resultado de la funcion para x: {x} es {fx}")

elif x < 10 and x <= 20:
    fx = x ** 2
    print(f"el resultado de la funcion para x: {x} es {fx}")

elif x < 20 and x <= 30:
    fx = x ** 2 + 5
    print(f"el resultado de la funcion para x: {x} es {fx}")

elif x < 30 and x <= 40:
    fx = x / 6 + x ** 2
    print(f"el resultado de la funcion para x: {x} es {fx}")

else: 
    x = 0
    fx = x
    print(f"el resultado de la funcion para x: {x} es {fx}")