from tablero import print_tablero
from parametros import RADIO_EXP

def bomba_x(tablero_propio, tablero_rival, radio):
    print("* * Tablero * *")
    print_tablero(tablero_rival, tablero_propio)
    print("\nInserte coordenadas de ataque (ColumnaFila): ", end = "")
    hundido = False
    ataque = input()
    if ataque[0].isdigit() or ataque[1].isdigit() == False:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_x(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    elif len(ataque) == 3:
        ataque = [int(ataque[1:3]),ord(ataque[0].upper())-65]
    else:
        ataque = [int(ataque[1]),ord(ataque[0].upper())-65]
    if ataque[0] > len(tablero_rival[0]) - 1:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_x(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    elif ataque[1] > len(tablero_rival):
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_x(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    if tablero_rival[ataque[0]][ataque[1]] == 'B' or tablero_rival[ataque[0]][ataque[1]] == ' ' :
        if tablero_rival[ataque[0]][ataque[1]] == 'B':
            tablero_rival[ataque[0]][ataque[1]] = 'F'
            hundido = True
        elif tablero_rival[ataque[0]][ataque[1]] == ' ':
            tablero_rival[ataque[0]][ataque[1]] = 'X'
        #hacia arriba
        ##hacia derecha
        fila_actual = ataque[0] - 1
        columna_actual = ataque[1] + 1
        por_rellenar = radio - 1
        while(fila_actual != -1 and columna_actual != len(tablero_rival[0]) and por_rellenar != 0):
            if tablero_rival[fila_actual][columna_actual] == ' ':
                tablero_rival[fila_actual][columna_actual] = "X"
            elif tablero_rival[fila_actual][columna_actual] == "B":
                tablero_rival[fila_actual][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            fila_actual = fila_actual - 1
            columna_actual = columna_actual + 1
        ##hacia izquierda
        fila_actual = ataque[0] - 1
        columna_actual = ataque[1] - 1
        por_rellenar = radio - 1
        while(fila_actual != - 1 and columna_actual != - 1 and por_rellenar != 0):
            if tablero_rival[fila_actual][columna_actual] == ' ':
                tablero_rival[fila_actual][columna_actual] = "X"
            elif tablero_rival[fila_actual][columna_actual] == "B":
                tablero_rival[fila_actual][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            fila_actual = fila_actual - 1
            columna_actual = columna_actual - 1
        #hacia abajo
        ##hacia derecha
        fila_actual = ataque[0] + 1
        columna_actual = ataque[1] + 1
        por_rellenar = radio - 1
        largo_filas = len(tablero_rival)
        largo_col = len(tablero_rival[0])
        while(fila_actual != largo_filas and columna_actual != largo_col and por_rellenar != 0):
            if tablero_rival[fila_actual][columna_actual] == ' ':
                tablero_rival[fila_actual][columna_actual] = "X"
            elif tablero_rival[fila_actual][columna_actual] == "B":
                tablero_rival[fila_actual][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            fila_actual = fila_actual + 1
            columna_actual = columna_actual + 1
        ##hacia izquierda
        fila_actual = ataque[0] + 1
        columna_actual = ataque[1] - 1
        por_rellenar = radio - 1
        while(fila_actual != len(tablero_rival) and columna_actual != - 1 and por_rellenar != 0):
            if tablero_rival[fila_actual][columna_actual] == ' ':
                tablero_rival[fila_actual][columna_actual] = "X"
            elif tablero_rival[fila_actual][columna_actual] == "B":
                tablero_rival[fila_actual][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            fila_actual = fila_actual + 1
            columna_actual = columna_actual - 1
    elif tablero_rival[ataque[0]][ataque[1]] == 'F':
        print("\nEse barco ya fue hundido. Intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_x(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    else:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_x(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    return(hundido, tablero_propio, tablero_rival)

def bomba_cruz(tablero_propio, tablero_rival, radio):
    print("* * Tablero * *")
    print_tablero(tablero_rival, tablero_propio)
    print("\nInserte coordenadas de ataque (ColumnaFila): ", end = "")
    hundido = False
    ataque = input()
    if ataque[0].isdigit() or ataque[1].isdigit() == False:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_cruz(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    elif len(ataque) == 3:
        ataque = [int(ataque[1:3]),ord(ataque[0].upper())-65]
    else:
        ataque = [int(ataque[1]),ord(ataque[0].upper())-65]
    if ataque[0] > len(tablero_rival[0]) - 1:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_cruz(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    elif ataque[1] > len(tablero_rival):
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_cruz(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    if tablero_rival[ataque[0]][ataque[1]] == 'B' or tablero_rival[ataque[0]][ataque[1]] == ' ':
        if tablero_rival[ataque[0]][ataque[1]] == 'B':
            tablero_rival[ataque[0]][ataque[1]] = 'F'
            hundido = True
        elif tablero_rival[ataque[0]][ataque[1]] == ' ':
            tablero_rival[ataque[0]][ataque[1]] = 'X'
        fila_actual = ataque[0] - 1
        por_rellenar = radio - 1 
        #hacia arriba
        while(fila_actual != -1 and por_rellenar != 0):
            if tablero_rival[fila_actual][ataque[1]] == ' ':
                tablero_rival[fila_actual][ataque[1]] = "X"
            elif tablero_rival[fila_actual][ataque[1]] == "B":
                tablero_rival[fila_actual][ataque[1]] = "F"
                hundido = True
            por_rellenar = por_rellenar-1
            fila_actual = fila_actual-1
        #hacia abajo
        fila_actual = ataque[0] + 1
        por_rellenar = radio - 1
        while(fila_actual != len(tablero_rival) and por_rellenar != 0):
            if tablero_rival[fila_actual][ataque[1]] == ' ':
                tablero_rival[fila_actual][ataque[1]] = "X"
            elif tablero_rival[fila_actual][ataque[1]] == "B":
                tablero_rival[fila_actual][ataque[1]] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            fila_actual = fila_actual + 1
        #hacia la derecha
        columna_actual = ataque[1] + 1
        por_rellenar = radio-1
        while(columna_actual != len(tablero_rival[0]) and por_rellenar != 0):
            if tablero_rival[ataque[0]][columna_actual] == ' ':
                tablero_rival[ataque[0]][columna_actual] = "X"
            elif tablero_rival[ataque[0]][columna_actual] == "B":
                tablero_rival[ataque[0]][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            columna_actual = columna_actual + 1
        #hacia la izquierda
        columna_actual = ataque[1] - 1
        por_rellenar=radio-1
        while(columna_actual != - 1 and por_rellenar != 0):
            if tablero_rival[ataque[0]][columna_actual] == ' ':
                tablero_rival[ataque[0]][columna_actual] = "X"
            elif tablero_rival[ataque[0]][columna_actual] == "B":
                tablero_rival[ataque[0]][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            columna_actual = columna_actual - 1
    elif tablero_rival[ataque[0]][ataque[1]] == 'F':
        print("\nEse barco ya fue hundido. Intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_cruz(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    else:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_cruz(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    return(hundido, tablero_propio, tablero_rival)

def bomba_diamante(tablero_propio, tablero_rival, radio):
    print("* * Tablero * *")
    print_tablero(tablero_rival, tablero_propio)
    print("\nInserte coordenadas de ataque (ColumnaFila): ", end = "")
    hundido = False
    ataque = input()
    if ataque[0].isdigit() or ataque[1].isdigit() == False:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_diamante(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    elif len(ataque) == 3:
        ataque = [int(ataque[1:3]),ord(ataque[0].upper())-65]
    else:
        ataque = [int(ataque[1]),ord(ataque[0].upper())-65]
    if ataque[0] > len(tablero_rival[0]) - 1:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_diamante(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    elif ataque[1] > len(tablero_rival):
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_diamante(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    if tablero_rival[ataque[0]][ataque[1]] == 'B' or tablero_rival[ataque[0]][ataque[1]] == ' ':
        if tablero_rival[ataque[0]][ataque[1]] == 'B':
            tablero_rival[ataque[0]][ataque[1]] = 'F'
            hundido = True
        elif tablero_rival[ataque[0]][ataque[1]] == ' ':
            tablero_rival[ataque[0]][ataque[1]] = 'X'
    ##linea principal
    ###derecha
        columna_actual = ataque[1] + 1
        por_rellenar = radio - 1
        while(columna_actual != len(tablero_propio[0]) and por_rellenar != 0):
            if tablero_rival[ataque[0]][columna_actual] == ' ':
                tablero_rival[ataque[0]][columna_actual] = "X"
            elif tablero_rival[ataque[0]][columna_actual] == "B":
                tablero_rival[ataque[0]][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            columna_actual = columna_actual + 1
    ###izquierda
        columna_actual = ataque[1] - 1
        por_rellenar = radio - 1
        while(columna_actual != - 1 and por_rellenar != 0):
            if tablero_rival[ataque[0]][columna_actual] == ' ':
                tablero_rival[ataque[0]][columna_actual] = "X"
            elif tablero_rival[ataque[0]][columna_actual] == "B":
                tablero_rival[ataque[0]][columna_actual] = "F"
                hundido = True
            por_rellenar = por_rellenar - 1
            columna_actual = columna_actual - 1
    #hacia arriba
    ##derecha
        fila_a_rellenar = ataque[0] - 1
        por_rellenar = radio - 2
        columna_actual = ataque[1] + 1
        por_rellenar2 = radio - 2
        largo_col = len(tablero_rival[0])
        while(fila_a_rellenar != - 1 and columna_actual != largo_col and por_rellenar != - 1):
            if tablero_rival[fila_a_rellenar][ataque[1]] == ' ':
                tablero_rival[fila_a_rellenar][ataque[1]] = "X"
            elif tablero_rival[fila_a_rellenar][ataque[1]] == "B":
                tablero_rival[fila_a_rellenar][ataque[1]] = "F"
                hundido = True
            while(por_rellenar2 != 0 and por_rellenar != 0):
                if tablero_rival[fila_a_rellenar][columna_actual] == ' ':
                    tablero_rival[fila_a_rellenar][columna_actual] = "X"
                elif tablero_rival[fila_a_rellenar][columna_actual] == "B":
                    tablero_rival[fila_a_rellenar][columna_actual] = "F"
                    hundido = True
                por_rellenar2 = por_rellenar - 1
                columna_actual = columna_actual + 1
            fila_a_rellenar = fila_a_rellenar - 1
            por_rellenar = por_rellenar - 1
            por_rellenar2 = por_rellenar
            columna_actual = ataque[1] + 1
    ##izquierda
        fila_a_rellenar = ataque[0] - 1
        por_rellenar = radio - 2
        columna_actual = ataque[1] - 1
        por_rellenar2 = radio - 2
        while(fila_a_rellenar != - 1 and columna_actual != - 1 and por_rellenar != -1):
            while(por_rellenar2 != 0 and por_rellenar != 0):
                if tablero_rival[fila_a_rellenar][columna_actual] == ' ':
                    tablero_rival[fila_a_rellenar][columna_actual] = "X"
                elif tablero_rival[fila_a_rellenar][columna_actual] == "B":
                    tablero_rival[fila_a_rellenar][columna_actual] = "F"
                    hundido = True
                por_rellenar2 = por_rellenar - 1
                columna_actual = columna_actual - 1
            fila_a_rellenar = fila_a_rellenar - 1
            por_rellenar = por_rellenar - 1
            por_rellenar2 = por_rellenar
            columna_actual = ataque[1] + 1
    #hacia abajo
    ##derecha
        fila_rellenar = ataque[0] + 1
        por_rellenar = radio - 2
        columna_actual = ataque[1] + 1
        por_rellenar2 = radio - 2
        largo_col = len(tablero_rival[0])
        largo_filas = len(tablero_rival)
        while(fila_rellenar != largo_filas and columna_actual != largo_col and por_rellenar != -1):
            if tablero_rival[fila_rellenar][ataque[1]] == ' ':
                tablero_rival[fila_rellenar][ataque[1]] = "X"
            elif tablero_rival[fila_rellenar][ataque[1]] == "B":
                tablero_rival[fila_rellenar][ataque[1]] = "F"
                hundido = True
            while(por_rellenar2 != 0 and por_rellenar != 0):
                if tablero_rival[fila_rellenar][columna_actual] == ' ':
                    tablero_rival[fila_rellenar][columna_actual] = "X"
                elif tablero_rival[fila_rellenar][columna_actual] == "B":
                    tablero_rival[fila_rellenar][columna_actual] = "F"
                    hundido = True
                por_rellenar2 = por_rellenar2 - 1
                columna_actual = columna_actual + 1
            fila_rellenar = fila_a_rellenar + 1
            por_rellenar = por_rellenar - 1
            por_rellenar2 = por_rellenar
            columna_actual = ataque[1] + 1
    ##izquierda
        fila_a_rellenar = ataque[0] + 1
        por_rellenar = radio - 2
        columna_actual = ataque[1] - 1
        por_rellenar2 = radio - 2
        largo_filas = len(tablero_rival)
        while(fila_a_rellenar != largo_filas and columna_actual != - 1 and por_rellenar != - 1):
            while(por_rellenar2 != 0 and por_rellenar != 0):
                if tablero_rival[fila_a_rellenar][columna_actual] == ' ':
                    tablero_rival[fila_a_rellenar][columna_actual] = "X"
                elif tablero_rival[fila_a_rellenar][columna_actual] == "B":
                    tablero_rival[fila_a_rellenar][columna_actual] = "F"
                    hundido = True
                por_rellenar2 = por_rellenar2 - 1
                columna_actual = columna_actual - 1
            fila_a_rellenar = fila_a_rellenar + 1
            por_rellenar = por_rellenar - 1
            por_rellenar2 = por_rellenar
            columna_actual = ataque[1] + 1
    elif tablero_rival[ataque[0]][ataque[1]] == 'F':
        print("\nEse barco ya fue hundido. Intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_diamante(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    else:
        print("\nCoordenadas invalidas, intente nuevamente.")
        print("\nApriete Enter para continuar", end = "")
        opcion = input()
        retornar = bomba_diamante(tablero_propio, tablero_rival, RADIO_EXP)
        return retornar
    return(hundido, tablero_propio, tablero_rival)