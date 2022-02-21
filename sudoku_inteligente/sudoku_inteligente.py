sudoku = [[8, 0, 0],
          [0, 5, 0], 
          [4 ,9 ,0]]

datos_disponibles = [1,2,3,4,5,6,7,8,9]
datos_usados = []
datos_por_usar = []
tamanio_matris = len(sudoku)

for iterador_matrix in range(tamanio_matris):
    print(sudoku[iterador_matrix])
print()
#Busca los valores que ya estan en la matriz
for fila in range(tamanio_matris):
    for columna in range(tamanio_matris):
        if sudoku[fila][columna] != 0:
            datos_usados.append(sudoku[fila][columna])
        
# Busca los valores que faltan por usar en la matriz 
for iterador_numero_faltante in datos_disponibles:          
    try:
        numero_encontrado = datos_usados.index(iterador_numero_faltante)
    except:
        numero_encontrado = -1        
    if numero_encontrado == -1:
        datos_por_usar.append(iterador_numero_faltante)
for fila in range(tamanio_matris):
    for columna in range(tamanio_matris):
        if sudoku[fila][columna] == 0:
            posicion_fila = fila
            posicion_columna = columna
            suma_fila = 0
            suma_columna = 0
            for colum in range(tamanio_matris):
                suma_fila = suma_fila + sudoku[posicion_fila][colum]
            for row in range(tamanio_matris):
                suma_columna = suma_columna + sudoku[row][posicion_columna]
            numero_a_ocupar = 0
            if suma_fila > suma_columna:
                numero_a_ocupar = 15 - suma_fila
                if numero_a_ocupar > 6: # 9 8 7 6 5 4 3 2 1
                    contador_decremento = 0
                    escape = 0
                    while escape == 0:
                        try:
                            error_numero_buscado = datos_por_usar.index(numero_a_ocupar)
                        except:
                            error_numero_buscado = -1
                            numero_a_ocupar -= 1
                        if error_numero_buscado != -1:
                            escape = 1
                            sudoku[posicion_fila][posicion_columna] = datos_por_usar[error_numero_buscado]
                            datos_por_usar.pop(error_numero_buscado)
                            for iterador_matrix in range(tamanio_matris):
                                print(sudoku[iterador_matrix])
                            print()
                        else:
                            contador_decremento += 1
                else:
                    error_numero_buscado = datos_por_usar.index(numero_a_ocupar)
                    sudoku[posicion_fila][posicion_columna]= datos_por_usar[error_numero_buscado]
                    datos_por_usar.pop(error_numero_buscado)
                    for iterador_matrix in range(tamanio_matris):
                        print(sudoku[iterador_matrix])
                    print()
            elif suma_columna > suma_fila:
                numero_a_ocupar = 15 - suma_columna
                if numero_a_ocupar > 6: # 9 8 7 6 5 4 3 2 1
                    contador_decremento = 0
                    escape = 0
                    while escape == 0:
                        try:
                            error_numero_buscado = datos_por_usar.index(numero_a_ocupar)
                        except:
                            error_numero_buscado = -1
                            numero_a_ocupar -= 1
                        if error_numero_buscado != -1:
                            escape = 1
                            sudoku[posicion_fila][posicion_columna] = datos_por_usar[error_numero_buscado]
                            datos_por_usar.pop(error_numero_buscado)
                            for iterador_matrix in range(tamanio_matris):
                                print(sudoku[iterador_matrix])
                            print()
                        else:
                            contador_decremento += 1
                else:
                    error_numero_buscado = datos_por_usar.index(numero_a_ocupar)
                    sudoku[posicion_fila][posicion_columna]= datos_por_usar[error_numero_buscado]
                    datos_por_usar.pop(error_numero_buscado)
                    for iterador_matrix in range(tamanio_matris):
                        print(sudoku[iterador_matrix])
                    print()

            else: 
                numero_a_ocupar = 15 - suma_columna
                error_numero_buscado = datos_por_usar.index(numero_a_ocupar)
                sudoku[posicion_fila][posicion_columna]= datos_por_usar[error_numero_buscado]
                datos_por_usar.pop(error_numero_buscado)
                for iterador_matrix in range(tamanio_matris):
                    print(sudoku[iterador_matrix])
                print()
#print(f'filas sin usar: {posicion_fila}')
#print(f'Columna sin usar: {posicion_columna}')
# ciclo para determinar que numero ya estamos usando 