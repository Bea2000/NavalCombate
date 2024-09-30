def menu_inicio():
    print("\n *** Menu de Inicio *** \n")
    print("[0] Iniciar una Partida")
    print("[1] Ver Ranking de Puntajes")
    print("[2] Salir \n")
    print("Selecciona una opcion: ", end = "")
    opcion = input()
    if opcion == "0":
        salir = iniciar_partida()
        return salir
    elif opcion == "1":
        salir = ranking_puntajes()
        return salir
    elif opcion == "2":
        return True
    else:
        print("\nLa opcion no es valida. Intente nuevamente.")
        print("Oprima Enter para continuar", end="")
        opcion = input()
        salir = menu_inicio()
        return salir

def iniciar_partida():
    print("\nIngresar un apodo: ", end = "")
    apodo = str(input())
    if apodo.isalnum() == True and len(apodo) >= 5:
        with open('puntajes.txt', 'a') as archivo:
            archivo.write("\n")
            archivo.write(apodo + ",")
        return apodo
    else:
        print("\nEl apodo debe tener mas de 5 dígitos y solo contener letras y números \n")
        print("[0] Volver")
        print("[1] Ir al Menu de Inicio \n")
        print("Ingrese una opción: ", end="")
        opcion = input()
        if opcion == "0":
            apodo = iniciar_partida()
            return apodo
        if opcion == "1":
            salir = menu_inicio()
            return salir
        else:
            print("\nLa opcion no es valida. Intente nuevamente.")
            print("Oprima Enter para continuar", end="")
            opcion = input()
            salir = menu_inicio()
            return salir

def dimensiones():
    print("\nIngrese las dimensiones del tablero (FilasxColumnas): ", end="")
    coordenadas = input()
    if 'x' not in coordenadas:
        print("\nEntrada inválida. Intente nuevamente.")
        print("\nApriete Enter para continuar: " ,end="")
        respuesta = input()
        coordenadas = dimensiones()
        return coordenadas
    coordenadas = coordenadas.split("x")
    if coordenadas[0].isdigit() == False:
        print("\nEntrada inválida. Intente nuevamente.")
        print("\nApriete Enter para continuar: " ,end="")
        respuesta = input()
        coordenadas = dimensiones()
        return coordenadas
    elif coordenadas[1].isdigit() == False:
        print("\nEntrada inválida. Intente nuevamente.")
        print("\nApriete Enter para continuar: " ,end="")
        respuesta = input()
        coordenadas = dimensiones()
        return coordenadas
    coordenadas = [int(coordenadas[0]),int(coordenadas[1])]
    if coordenadas[0] < 3 or coordenadas[0] > 15:
        print("\nLas coordenadas deben estar entre 3 y 15. Intente nuevamente.")
        print("\nApriete Enter para continuar: ", end="")
        respuesta = input()
        coordenadas = dimensiones()
        return coordenadas
    elif coordenadas[1] < 3 or coordenadas[1] > 15:
        print("\nLas coordenadas deben estar entre 3 y 15")
        print("\nApriete Enter para continuar: " ,end="")
        respuesta = input()
        coordenadas = dimensiones()
        return coordenadas
    elif coordenadas[0] >= 3 and coordenadas[1] >= 3:
        if coordenadas[0] <= 15 and coordenadas[1] <= 15:
            return coordenadas
    else:
        print("\nEntrada inválida. Intente nuevamente.")
        print("\nApriete Enter para continuar: " ,end="")
        respuesta = input()
        coordenadas = dimensiones()
        return coordenadas
        
def ranking_puntajes():
    archivo = open('puntajes.txt')
    puntajes = archivo.readlines()
    archivo.close()
    puntajes = [puntaje.strip().split(",") for puntaje in puntajes]
    for puntaje in puntajes:
        puntaje[1] = int(puntaje[1])
    top_5 = []
    mayor = True
    while len(top_5) < 5 and len(puntajes) != 0:
        if mayor == True:
            i = 0
        if len(puntajes) == 1:
            top_5.append(puntajes[0])
            puntajes.pop(0)
        while i < len(puntajes):
            j = 0
            mayor = True
            while j < len(puntajes):
                if j == i:
                    pass
                elif puntajes[i][1] < puntajes[j][1]:
                    mayor = False
                j=j+1
            if mayor == True:
                top_5.append(puntajes[i])
                puntajes.pop(i)
                i = len(puntajes)
            else:
                i = i + 1
    i = 1     
    print("\n*** Ranking de Puntajes *** \n")
    while len(top_5) != 0:
        print(str(i) + ")", top_5[0][0] + ":", top_5[0][1])
        top_5.pop(0)
        i=i+1
    print("\n[0] Volver \n")
    print("Ingresar opcion: ", end="")
    opcion = input()
    if opcion == "0":
        salir = menu_inicio()
        return salir
    else:
        print("\nLa opcion no es valida. Intente nuevamente.")
        print("Oprima Enter para continuar", end="")
        opcion = input()
        ranking_puntajes()
