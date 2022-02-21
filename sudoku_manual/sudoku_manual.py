sudoku = [[8, 0, 0],
          [0, 5, 0], 
          [4 ,9 ,0]]
sudoku_finalizado = 0
datos_usados = []
datos_aceptados = [1,2,3,4,5,6,7,8,9]
datos_faltantes = []
for random in range(len(sudoku)):
    print(sudoku[random])
for row in range(len(sudoku)):
    for colum in range(len(sudoku)):
        if sudoku[row][colum] != 0:
            datos_usados.append(sudoku[row][colum])
for buscador in datos_aceptados:
    try:
        numero_buscado = datos_usados.index(buscador)
    except:
        numero_buscado = -1
    if numero_buscado == -1:
        datos_faltantes.append(buscador)


dato_fila = int(input("\nIngrese la posicion de la fila: "))
dato_columna = int(input("\nIngrese la posicion de la columna: "))
numero_a_colocar = int(input("\nIngrese el numero en esa posicion: "))


while sudoku_finalizado == 0:
    escape = 0
    while escape == 0:
        try:
            error_numero_no_encontrado = datos_faltantes.index(numero_a_colocar)
        except:
            error_numero_no_encontrado = -1

        if error_numero_no_encontrado == -1:
            print(f'''
            El numero {numero_a_colocar} ya se ha usado
            Introdusca otro numero
            ''')
            numero_a_colocar = int(input("\nIngrese el  numero en esa posicion: "))
            escape = 0
        else:
            escape = 1
        
        if sudoku[dato_fila][dato_columna] != 0:
            print(f'''
            La posicion en la fila {dato_fila} y en la columna {dato_columna}
            esta ocupado.
            Ingrese nuevos valores para la fila y la columa
            ''')
            dato_fila = int(input("\nIngrese la posicion de la fila: "))
            dato_columna = int(input("\nIngrese la posicion de la columna: "))
            escape = 0
        else: 
            escape = 1

        if escape == 1:
            print("\nDatos Correctos\n")

    sudoku[dato_fila][dato_columna] = numero_a_colocar    
    datos_usados.append(numero_a_colocar)
    datos_faltantes.pop(error_numero_no_encontrado)
        
    comprobar_numero = 0
    suma_fila = 0
    suma_columna = 0

    for iterador in range(len(sudoku)):
        suma_fila += sudoku[dato_fila][iterador]
        suma_columna += sudoku[iterador][dato_columna]
    if suma_fila > 15 or suma_columna > 15:
        print(f'''\nEl numero {numero_a_colocar} en la posicion 
        fila: {dato_fila}, columna: {dato_columna} es incorrecto''')
        datos_usados.pop(datos_usados.index(numero_a_colocar))
        datos_faltantes.append(numero_a_colocar)
        sudoku[dato_fila][dato_columna] = 0
    else:
        for random in range(len(sudoku)):
            print(sudoku[random])

    suma_fila_0 = 0
    suma_fila_1 = 0
    suma_fila_2 = 0
    suma_columna_0 = 0
    suma_columna_1 = 0
    suma_columna_2 =0

    for row in range(len(sudoku)):
        for column in range(len(sudoku)):
            if row == 0:
                suma_fila_0 += sudoku[row][column]
            elif row == 1: 
                suma_fila_1 += sudoku[row][column]
            else: 
                suma_fila_2 += sudoku[row][column]
    for column in range(len(sudoku)):
        for row in range(len(sudoku)):
            if column == 0:
                suma_columna_0 += sudoku[row][column]
            elif column == 1:
                suma_columna_1 += sudoku[row][column]
            else:
                suma_columna_2 += sudoku[row][column]

    if suma_fila_0 and suma_fila_1 and suma_fila_2 and suma_columna_0 and suma_columna_1 and suma_columna_2 == 15:
        sudoku_finalizado = 1
        print('\nSudoku correcto')
    else:
        sudoku_finalizado = 0
        dato_fila = int(input("\nIngrese la posicion de la fila: "))
        dato_columna = int(input("\nIngrese la posicion de la columna: "))
        numero_a_colocar = int(input("\nIngrese el numero en esa posicion: "))