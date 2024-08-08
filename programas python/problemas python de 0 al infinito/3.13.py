color = str(input("Ingrese el color de la piña "))
aroma = str(input("Ingrese el aroma de su piña "))
peso = float(input("Ingrese el peso de su piña "))

if peso < 2.2:
    peso = False

else:
    peso = True

if color == "dorado" and aroma == "suave" and peso == True:
    print("su piña es madura, ahora metasela en el ano")

else:
    print("haber estudiado chaval")

