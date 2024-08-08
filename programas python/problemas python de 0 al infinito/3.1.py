nota = int(input("ingrese la nota del alumno "))

while nota < 1 or nota > 10:
    nota = int(input("ingrese una nota valida para el alumno "))

if nota >= 6:
    print("el alumno aprobo anazi")

else:
    print("el alumno deasaprobo tambien anazi")