# Definir la matriz bidimensional
matriz = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, None, None

# Valor a buscar en la matriz
valor_a_buscar = 5

# Realizar la búsqueda en la matriz
encontrado, fila, columna = buscar_valor(matriz, valor_a_buscar)

# Imprimir el resultado de la búsqueda
if encontrado:
    print(f"El valor {valor_a_buscar} fue encontrado en la fila {fila+1} y columna {columna+1}.")
else:
    print(f"El valor {valor_a_buscar} no fue encontrado en la matriz.")