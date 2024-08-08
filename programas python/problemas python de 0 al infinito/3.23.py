n1 = int(input("ingrese su n1 "))
n2 = int(input("ingrese su n2 "))
n3 = int(input("ingrese su n3 "))


if  n1 > n3 and n1 > n2:
    if n1 == n3:
        print(f"los mayores son {n1} y {n3}")
        if n1 == n2:
            print(f"los mayores son {n1} y {n2}")
        else:
            print(f"el mayor es {n1}")
    
if n2 > n1 and n2 > n3:
  if n2 == n3:
        print(f"los mayores son {n2} y {n3}")
        if n1 == n1:
            print(f"los mayores son {n2} y {n1}")
        else:
            print(f"el mayor es {n2}")

if n3 > n1 and n3 > n2:
   if n3 == n1:
        print(f"los mayores son {n3} y {n1}")
        if n3 == n2:
            print(f"los mayores son {n3} y {n2}")
        else:
            print(f"el mayor es {n3}")


