# str.format es un metodo que se utiliza para formatear las impresiones 

edad = 86

print("edad del abuelo: {0:5d}" .format(edad))

""" ("texto {i:jd}" .format(variable o expresion entera)) """

"""" 
donde i: es un numero entero, indica el primer valor a imprimir, el segundo, etc
      j: es un numero entero, indica la cantidad de espacios reservados para el numero y se justifica a la derecha
      d: es la letra d, indica que es un numero entero lo que se imprimira 
      en el () del format se incluira la variable cuyo contenido se quiere imprimir, tambien se puede poner una constante o, una expresion que al evaluarse genere un numero entero 
 """


# Otro ejemplo de uso del método .format()
nombre = "Juan"
edad = 30

# Formatear una cadena usando .format()
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)

"""en el caso de los numeros reales, la manera de darles formato varia un poco porque esta incluye las especificaciones sobre la cantidad de decimales que se tomaran en cuenta
    en general se utiliza la siguiente sintaxis """

#  "texto {i:j.kf}" .format(variable o expresion real) 

"""donde i: es un numero entero, indica el primer valor a imprimir, el segundo, etc
         j: es un numero entero, indica la cantidad de espacios reservados para el numero y se justifica a la derecha. 
         este elemento es opcional (j) si no se da o su valor es mas pequeño que la cantidad de digitos que tiene el numero, entonces se escribe justificado a la izquierda, sin perder ninguno de sus digitos
         k: es un numero entero, indica la cantidad de decimales que se imprimiran. completa con 0 si es necesario 
         f: es la letra f, indica que es un numero real lo que se imprimira"""


### digamos, lo que esta encerrado entre las llaves delimita el lugar donde se imprimira lo que mandemos atraves de la variable encerrada en el parentesis de .format()

"""en todos los ejemplos anteriores se usaron argumentos proposicionales, es decir, por medio del primer puesto en {} se coloco la posicion en la que se imprimirian los datos
   otra forma de hacerlo es por medio de argumentos nombrados, es decir entre las {} se da el nombre del argumento por el cual sera sustituido """

print("edad del abuelo: {edad:5d} " .format(edad = 88))

print("este {herramienta} es de color {color}.".format(herramienta= "martillo" , color= "gris"))

print("este {0} es de color {1}.".format("martillo" , "gris"))


"""otra forma de dar formato a las impresiones son las f-strings """

altura = 1.75

valor = 'altura'

print(f'la {valor} del abuelo es {altura:.1f}m') #da formato al numero

nombre  = 'Alberto'

print(f'Te dije que se llama {nombre!r}')

#!r provoca que el valor nombre se escriba entre '', se vera 'Alberto'

"""tambien se puede definir un formato previamente y luego simplemente llamar al formato en el print.
    el <10 reserva 10 espacios para el valor de la variable """

formato1 = f'{valor:<10} = {altura:.2f}'

print(formato1)


formato2 = f'{"peso".capitalize()} = {59.605:.2f}'

print(formato2)

"""la funcion capitalize() se utiliza para convertir la primera letra de una cadena (string) en mayuscula y el resto en minusculas"""


