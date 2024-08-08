print("Ingrese su nombre completo, nombre, apellido, segundo apellido")

nombre_completo = str(input("Ingrese su nombre "))

espacio = nombre_completo.find('')

nombre = nombre_completo[0:espacio:]

nombre_completo = nombre_completo[espacio + 1:]

espacio = nombre_completo.find('')

primer_apellido = nombre_completo[:espacio]

segundo_apellido = nombre_completo[espacio + 1:]

nombre_reordenado = primer_apellido + '' + segundo_apellido + ',' + nombre

print(nombre_reordenado)