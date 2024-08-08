#cadenas
cadena_or = str(input("ingrese su cadena "))

cadenamis = cadena_or.lower()

primerale = cadenamis[0]

segundale = cadenamis[1]

"""MUCHO MAS FACIL"""

recortecadena = cadena_or[0:2]

nuevacadena = cadenamis[2:] + primerale +segundale

print(nuevacadena)