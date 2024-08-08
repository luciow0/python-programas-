n = int(input("Ingrese la cantidad de alumnos"))
mayor = -1
menor = 11
promedio = 0



for i in range(n):
    matricula = int(input("ingrese la matricula del alumno "))
    notas = float(input("ingrese el promedio del alumnno"))

    promedio += notas

    if notas > mayor:
        mayor = notas
        alumno_mayor = matricula
    
    if notas < menor:
        menor = notas
        alumno_menor = matricula

print(f"el alumno con el promedio mas alto fue el alumno {alumno_mayor} con un promedio de {mayor}, el alumno con promedio mas bajo fue {alumno_menor} con un promedio de {menor} y el promedio grupal es de {promedio / n}")
    