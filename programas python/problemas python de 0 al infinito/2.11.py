largo = float(input("ingrese el largo del terreno en metros "))

ancho = float(input("ingrese el ancho del terreno en metros "))

totalTerreno = largo * ancho 

cantPlantas = largo / 0.25

cantLineas = ancho / 0.3

total = cantPlantas * cantLineas

print("total de plantas que entraran en el terreno {total:.}")