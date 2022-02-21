sudoku = [[8, 0, 0],
          [0, 5, 0], 
          [4 ,9 ,0]]


def agregar(matris, indice_fila, indice_columna, numero_agregar):
    matris[indice_fila][indice_columna] = numero_agregar
    return matris

sudoku = agregar(sudoku, 0, 1, 2)

for i in range(3):
    print(sudoku[i])

lista = [1,2,3,4,5]

lista.pop()