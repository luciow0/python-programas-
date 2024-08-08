def crear_matriz_grande(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Puedes agregar cualquier valor que desees aquí, como i * j para tener una matriz con valores específicos
            fila.append(0)
        matriz.append(fila)
    return matriz

def main():
    # Especifica el tamaño de la matriz
    filas = 10000000
    columnas = 10000000

    # Crea la matriz grande
    matriz_grande = crear_matriz_grande(filas, columnas)

    # Muestra la matriz
    print("Matriz grande creada con éxito.")

if __name__ == "__main__":
    main()
