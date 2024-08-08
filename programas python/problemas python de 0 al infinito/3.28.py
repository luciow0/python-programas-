clave = str(input("Ingreses su clave de empleado "))
antiguedad = int(input("Ingrese su antiguedad como empleado "))
categoria = int(input("Ingrese su categoria de empleado "))

if categoria == 3 or categoria == 5: 
    if antiguedad >= 5:
        print(f"el empleado {clave} es apropiado para el cargo")

elif categoria == 2 and antiguedad >= 10:
    print(f"el empleado {clave} es apropiado para el cargo")

else:
    print("el empleado no es apropiado para el puesto segun las caracteristicas solicitadas")