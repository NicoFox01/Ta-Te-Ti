#Funcion de inicio de juego.
def start_game():
    print("¡Empecemos!")
    print("¡Te enseño como jugar! La consola será la X y tú seras el O. Una vez por turno, iran colocando su figura en los siguientes casilleros. ¡El que coloque 3 en línea, gana!")
    for fila in tablero:
        print(fila)
    game_loop()
    
def check_winner():
    # Lista de combinaciones ganadoras
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]

    # Gana PC.
    for combinacion in combinaciones_ganadoras:
        if lista_copia[combinacion[0]] == lista_copia[combinacion[1]] == lista_copia[combinacion[2]] == 'X':
            return print("La PC gana")
            break
    # Gana User.
    for combinacion in combinaciones_ganadoras:
        if lista_copia[combinacion[0]] == lista_copia[combinacion[1]] == lista_copia[combinacion[2]] == 'O':
            return print("¡Has ganado!")
            break
    return None  # Nadie ha ganado todavía        

#Turno de la PC
def pc_turn():
    import random

    # Elegir un valor que no sea 'X' ni 'O'
    pc_value = random.choice([valor for valor in lista_copia if valor not in ['X', 'O']])
    
    print("La PC elige:", pc_value)
    indice = lista_copia.index(pc_value)
    lista_copia[indice] = 'X'
    update_board()
    resultado = check_winner()
    if resultado:
        print(resultado)
        
# Turno del Usuario
def user_turn():
    user_value = input("Elije uno de los casilleros libres:")
    if user_value in lista_copia:
        indice = lista_copia.index(user_value)
        lista_copia[indice] = 'O'
        update_board()
        resultado = check_winner()
        if resultado:
            print(resultado)
    else:
        user_value = input("Elige un casillero libre:")
        
# Función loop del juego
turno_actual = 1
total_turnos = 9

def game_loop():
    while turno_actual < total_turnos:
        pc_turn()
        resultado = check_winner()
        if resultado:
            print(resultado)
            break

        user_turn()
        resultado = check_winner()
        if resultado:
            print(resultado)
            break

        turno_actual += 2  # Incrementar el conteo de turnos para la PC y el usuario

    if turno_actual >= total_turnos:
        print("El juego ha terminado. Empate.")
        
# Impresión y Actualizacion del tablero
def print_board():
    for fila in tablero:
        print(fila)
    
def update_board():
    indice_lista = 0
    for i in range(3):
        for j in range(3):
            tablero[i][j] = lista_copia[indice_lista]
            indice_lista += 1
    print_board()
    
#Loop de juego
def game_loop():
    while True:
        pc_turn()
        resultado = check_winner()
        if resultado:
            print(resultado)
            break

        user_turn()
        resultado = check_winner()
        if resultado:
            print(resultado)
            break

        if len([casillero for casillero in lista_copia if casillero.isdigit()]) == 0:
            print("Empate. ¡Nadie ha ganado!")
            break          
        
#Lista + tablero + copia de lista        
lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_copia = lista
tablero = [['' for _ in range(3)] for _ in range(3)]
indice_lista = 0
for i in range(3):
    for j in range(3):
        tablero[i][j] = lista_copia[indice_lista]
        indice_lista += 1
        
#Funcion de inicio de Juego
while True:
    action_game = input("¿Quieres empezar a jugar? 'si' o 'no' ").lower()
    if action_game == "si":
        start_game()
        break
    elif action_game == "no":
        print("Muchas gracias por tu respuesta. Terminamos el juego.")
        break
    else:
        print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")
