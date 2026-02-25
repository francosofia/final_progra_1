def tateti():
    # Crear matriz 3x3 correctamente (cada fila independiente)
    matriz = [["-" for _ in range(3)] for _ in range(3)]
    
    turno = "X"  # Player 1 empieza
    flag_partida = True
    
    def mostrar_tablero():
        # Muestra el tablero en consola
        for fila in matriz:
            print(" ".join(fila))
        print()
    
    def hay_ganador():
        # Verifica filas
        for fila in matriz:
            if fila[0] == fila[1] == fila[2] != "-":
                return True
        
        # Verifica columnas
        for col in range(3):
            if matriz[0][col] == matriz[1][col] == matriz[2][col] != "-":
                return True
        
        # Verifica diagonales
        if matriz[0][0] == matriz[1][1] == matriz[2][2] != "-":
            return True
        
        if matriz[0][2] == matriz[1][1] == matriz[2][0] != "-":
            return True
        
        return False
    
    def tablero_lleno():
        # Verifica si ya no hay espacios libres
        for fila in matriz:
            if "-" in fila:
                return False
        return True
    
    while flag_partida:
        mostrar_tablero()
        
        if turno == "X":
            print("Turno Player 1 (X)")
        else:
            print("Turno Player 2 (O)")
        
        try:
            fila = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
        except ValueError:
            print("Entrada inválida. Ingrese números.")
            continue
        
        # Validar rango
        if fila not in range(3) or col not in range(3):
            print("Posición fuera de rango.")
            continue
        
        # Validar casilla libre
        if matriz[fila][col] != "-":
            print("Casilla ocupada, elija otra.")
            continue
        
        # Colocar ficha
        matriz[fila][col] = turno
        
        # Verificar ganador
        if hay_ganador():
            mostrar_tablero()
            if turno == "X":
                print("¡Ganó Player 1!")
            else:
                print("¡Ganó Player 2!")
            flag_partida = False
        
        # Verificar empate
        elif tablero_lleno():
            mostrar_tablero()
            print("¡Empate!")
            flag_partida = False
        
        # Cambiar turno
        else:
            turno = "O" if turno == "X" else "X"
    
    return matriz

print(tateti())