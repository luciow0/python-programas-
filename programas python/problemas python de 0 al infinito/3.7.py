p = int(input("ingrese el valor de p"))
q = int(input("ingrese el valor de q"))

resu = (p ** 3 + q ** 3) - (2 * p * q ** 2)

if resu < 970:
    print("valor de p ",p,"valor de q",q)