from menu_inicio import dimensiones, menu_inicio
from bombas_especiales import bomba_x, bomba_diamante, bomba_cruz
from tablero import print_tablero
from parametros import NUM_BARCOS, RADIO_EXP
import random
import copy

def menu_de_juego(tablero_propio, tablero_rival):
    terminar = revisar_termino_juego(tablero_propio, tablero_rival)
    if terminar == False:
        print("\n - - Menu de juego - -\n")
        print_tablero(tablero_rival, tablero_propio)
        print("\n[0] Rendirse")
        print("[1] Lanzar una bomba")
        print("[2] Salir del programa")
        print("\nIngresa tu elección: ", end="")
        opcion = input()
        if opcion == "0":
            puntaje = calcular_puntaje(tablero_propio, tablero_rival)
            print("Tu puntaje ha sido de ", end = "")
            print(puntaje)
            opcion = menu_inicio()
            if opcion != True:
                coordenadas = dimensiones()
                tableros = crear_tablero(coordenadas)
                tablero_rival = tableros[0]
                tablero_propio = tableros[1]
                menu_de_juego(tablero_propio, tablero_rival)
        elif opcion == "1":
            turno_jugador(tablero_propio, tablero_rival)
        elif opcion == "2":
            archivo = open("puntajes.txt")
            lineas = archivo.readlines()
            lineas = lineas[:-1]
            archivo.close()
            archivo = open("puntajes.txt",'w')
            archivo.writelines([puntaje for puntaje in lineas])
            archivo.close()
        else:
            print("Ingrese una opción válida")
            print("Apriete Enter para continuar", end="")
            opcion = input()
            menu_de_juego(tablero_propio, tablero_rival)
    else:
        return tablero_propio,tablero_rival

def crear_tablero(dimensiones):
    tablero = []
    for i in range(0,dimensiones[0]):
        fila = []
        for j in range(0,dimensiones[1]):
            fila.append(" ")
        tablero.append(fila)
    #tablero propio
    tablero_propio = copy.deepcopy(tablero)
    i = 0
    while i < NUM_BARCOS:
        eleccion_fila = random.randint(0,dimensiones[0]-1)
        eleccion_columna = random.randint(0,dimensiones[1]-1)
        if tablero_propio[eleccion_fila][eleccion_columna] == 'B':
            pass
        else:
            tablero_propio[eleccion_fila][eleccion_columna] = 'B'
            i = i + 1
    #tablero rival
    tablero_rival = copy.deepcopy(tablero)
    i = 0
    while i < NUM_BARCOS:
        eleccion_fila = random.randint(0,dimensiones[0]-1)
        eleccion_columna = random.randint(0,dimensiones[1]-1)
        if tablero_rival[eleccion_fila][eleccion_columna] == 'B':
            pass
        else:
            tablero_rival[eleccion_fila][eleccion_columna] = 'B'
            i = i + 1
    return [tablero_rival, tablero_propio]

def turno_jugador(tablero_propio, tablero_rival):
    terminar = revisar_termino_juego(tablero_propio, tablero_rival)
    if terminar == False:
        print("\n[0] Bomba regular")
        print("[1] Bomba especial")
        print("\nElegir tipo de bomba: ", end = "")
        opcion = input()
        if opcion == "0":
            salir = bomba_regular(tablero_propio, tablero_rival)
            return salir
        if opcion == "1":
            if uso_bomba_especial == False:
                salir = bomba_especial(tablero_propio, tablero_rival)
                return salir
            else:
                print("\nYa utilizaste tu bomba especial.")
                turno_jugador(tablero_propio, tablero_rival)
        else:
            print("\nLa opción no es válida.", end = "")
            print("Apriete Enter para continuar.", end = "")
            opcion = input()
            turno_jugador(tablero_propio, tablero_rival)
    else:
        return tablero_propio,tablero_rival

def bomba_regular(tablero_propio, tablero_rival):
    terminar = revisar_termino_juego(tablero_propio, tablero_rival)
    if terminar == False:
        print("\n* * Tablero * *")
        print_tablero(tablero_rival, tablero_propio)
        print("\nInserte coordenadas de ataque (ColumnaFila): ", end = "")
        ataque = input()
        if ataque[0].isdigit() or ataque[1].isdigit() == False:
            print("\nCoordenadas invalidas, intente nuevamente.")
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            retornar = bomba_regular(tablero_propio, tablero_rival)
            return retornar
        elif len(ataque) == 3:
            ataque = [int(ataque[1:3]),ord(ataque[0].upper())-65]
        else:
            ataque = [int(ataque[1]),ord(ataque[0].upper())-65]
        if ataque[0] > len(tablero_rival[0]) - 1:
            print("\nCoordenadas invalidas, intente nuevamente.")
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            retornar = bomba_regular(tablero_propio, tablero_rival)
            return retornar
        elif ataque[1] > len(tablero_rival):
            print("\nCoordenadas invalidas, intente nuevamente.")
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            retornar = bomba_regular(tablero_propio, tablero_rival)
            return retornar
        if tablero_rival[ataque[0]][ataque[1]] == 'B':
            print("\nLe has dado!") 
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            tablero_rival[ataque[0]][ataque[1]] = 'F'
            menu_de_juego(tablero_propio, tablero_rival)
        elif tablero_rival[ataque[0]][ataque[1]] == 'F':
            print("\nEse barco ya fue hundido. Intente nuevamente.")
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            retornar = bomba_regular(tablero_propio, tablero_rival)
            return retornar
        elif tablero_rival[ataque[0]][ataque[1]] == ' ':
            print("\nHaz fallado, suerte para la proxima.")
            tablero_rival[ataque[0]][ataque[1]] = 'X'
            print("\nEs el turno de tu rival!")
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            turno_rival(tablero_propio, tablero_rival)
        else:
            print("\nCoordenadas invalidas, intente nuevamente.")
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            retornar = bomba_regular(tablero_propio, tablero_rival)
            return retornar
    else:
        return tablero_propio,tablero_rival

def bomba_especial(tablero_propio, tablero_rival):
    print("\n[0] Bomba Cruz")
    print("[1] Bomba X")
    print("[2] Bomba Diamante")
    print("\nSelecciona una opción: ", end = "")
    opcion = input()
    if opcion == "0":
        usada_bomba_especial()
        var = bomba_cruz(tablero_propio, tablero_rival, RADIO_EXP)
        hundido = var[0]
        tablero_propio = var[1]
        tablero_rival = var[2]
        if hundido == True:
            menu_de_juego(tablero_propio,tablero_rival)
        else:
            print("\nNo le has dado a ningun barco. Suerte para la proxima")
            turno_rival(tablero_propio, tablero_rival)
    elif opcion == "1":
        usada_bomba_especial()
        var = bomba_x(tablero_propio, tablero_rival, RADIO_EXP)
        hundido = var[0]
        tablero_propio = var[1]
        tablero_rival = var[2]
        if hundido == True:
            menu_de_juego(tablero_propio,tablero_rival)
        else:
            print("\nNo le has dado a ningun barco. Suerte para la proxima")
            turno_rival(tablero_propio, tablero_rival)
    elif opcion == "2":
        usada_bomba_especial()
        var = bomba_diamante(tablero_propio, tablero_rival, RADIO_EXP)
        hundido = var[0]
        tablero_propio = var[1]
        tablero_rival = var[2]
        if hundido == True:
            menu_de_juego(tablero_propio,tablero_rival)
        else:
            print("\nNo le has dado a ningun barco. Suerte para la proxima")
            turno_rival(tablero_propio, tablero_rival)
    else:
        return tablero_propio,tablero_rival

def turno_rival(tablero_propio, tablero_rival):
    terminar = revisar_termino_juego(tablero_propio, tablero_rival)
    if terminar == False:
        ataque = ["",""]
        ataque[0] = int(random.randint(0,len(tablero_propio) - 1))
        ataque[1] = int(random.randint(0,len(tablero_propio[0]) - 1))
        if tablero_propio[ataque[0]][ataque[1]] == 'B':
            print("\nTu rival le a dado a tu barco en",chr(int(ataque[1])+65)+str(ataque[0]))
            tablero_propio[ataque[0]][ataque[1]] = 'F'
            print("\nEl tablero actual es:")
            print_tablero(tablero_rival, tablero_propio)
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            retornar = turno_rival(tablero_propio, tablero_rival)
            return retornar
        elif tablero_propio[ataque[0]][ataque[1]] == 'F':
            retornar = turno_rival(tablero_propio, tablero_rival)
            return retornar
        elif tablero_propio[ataque[0]][ataque[1]] == ' ':
            print("\n¡Tu rival ha fallado!")
            tablero_propio[ataque[0]][ataque[1]] = 'X'
            print("\nApriete Enter para continuar", end = "")
            opcion = input()
            menu_de_juego(tablero_propio, tablero_rival)
        elif tablero_propio[ataque[0]][ataque[1]] == 'X':
            retornar = turno_rival(tablero_propio, tablero_rival)
            return retornar
    else:
        return tablero_propio,tablero_rival

def revisar_termino_juego(tablero_propio, tablero_rival):
    terminar = True
    for fila in tablero_propio:
        for columna in fila:
            if columna == 'B':
                terminar = False
        if terminar == True:
            return terminar
    if terminar == False:
        terminar = True
        for fila in tablero_rival:
            for columna in fila:
                if columna == 'B':
                    terminar = False
        return terminar
    else:
        return tablero_propio, tablero_rival

def ganador(tablero_propio):
    ganador = True
    for fila in tablero_rival:
        for columna in fila:
            if columna == 'B':
                ganador = False
    return ganador

def calcular_puntaje(tablero_propio, tablero_rival):
    filas = len(tablero_propio)
    columnas = len(tablero_propio[0])
    total_hundidos_j = 0
    for fila in tablero_propio:
        total_hundidos_j += fila.count("F")
    total_hundidos_r = 0
    for fila in tablero_rival:
        total_hundidos_r += fila.count("F")
    puntaje = filas * columnas * NUM_BARCOS * (total_hundidos_r - total_hundidos_j)
    if 0 > puntaje:
        puntaje = 0
    with open('puntajes.txt', 'a') as archivo:
        archivo.write(str(puntaje))
    return puntaje

def usada_bomba_especial():
    global uso_bomba_especial
    uso_bomba_especial = True
    return True

uso_bomba_especial = False
salir = menu_inicio()
if salir == True:
    pass
else:
    coordenadas = dimensiones()
    tableros = crear_tablero(coordenadas)
    tablero_rival = tableros[0]
    tablero_propio = tableros[1]
    menu_de_juego(tablero_propio, tablero_rival)
    terminar = revisar_termino_juego(tablero_propio, tablero_rival)
    if terminar == True:
        puntaje = calcular_puntaje(tablero_propio, tablero_rival)
        ganador = ganador(tablero_propio)
        if ganador == True:
            print("\nHaz ganado!!")
        elif ganador == False:
            print("Haz perdido...suerte para la próxima")
        print("Tu puntaje ha sido de ", end = "")
        print(puntaje)
    else:
        pass