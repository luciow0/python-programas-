frase_inicial = str(input())

fraseupper = frase_inicial.upper()

n = len(fraseupper)

frase_codificada = fraseupper.replace('a' , '1')
frase_codificada = fraseupper.replace('e' , '3')
frase_codificada = fraseupper.replace('i' , '5')
frase_codificada = fraseupper.replace('o' , '7')
frase_codificada = fraseupper.replace('u' , '9')



mitad = n // 2

primer_mitad = frase_codificada[0:mitad]

segunda_mitad = frase_codificada[mitad:]

frase_final = segunda_mitad + primer_mitad

print(frase_final)