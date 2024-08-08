nomina = 0

for i in range (0,10,1):
    sueldo = float(input("Ingrese su sueldo "))
    nomina += sueldo

print(f"la nomina de la empresa es {nomina:.2f}")
