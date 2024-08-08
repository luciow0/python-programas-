peso = float(input("Ingrese su peso en Kg "))
estatura = float(input("ingrese su estatura en metros "))

imc = peso / (estatura ** 2)

if imc <= 18.5:
    print("usted sufre de flaco raquitico")

