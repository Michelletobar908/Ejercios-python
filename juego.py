import random

# Instrucciones del juego
print("Bienvenido al juego de Piedra, papel o tijeras. Tendremos 3 rondas para ver quién gana más veces.")

# Puntajes iniciales
user_score = 0
#almacena el puntaje
computer_score = 0

# Nombre del usuario
user_name = input("Por favor, introduce tu nombre: ")

# Juego de 3 rondas
for i in range(3):
    print(f"Ronda {i+1} - ¡{user_name} elige tu opción!")
    #el for crea el ciclo de las randas y la variable almacena la espuesta 
    user_choice = input("¿Piedra, papel o tijeras? ").lower()
    
    # Elección aleatoria de la computadora
    options = ["piedra", "papel", "tijeras"]
    computer_choice = random.choice(options)
    print(f"La computadora elige {computer_choice}.")
    
    # Determinar el ganador
        #verifica si son iguales 
    if user_choice == computer_choice:
        print("Empate. Nadie obtiene puntos.")
        #verifica las diferentes opciones 
    elif (user_choice == "piedra" and computer_choice == "tijeras") or (user_choice == "papel" and computer_choice == "piedra") or (user_choice == "tijeras" and computer_choice == "papel"):
        print(f"¡Gana {user_name}!")
        user_score += 1
        #sino es verdaderia la funcion anterior 
    else:
        print("Gana la computadora.")
        computer_score += 1

# Resultado final
print("¡Juego terminado!")
print(f"{user_name} obtuvo {user_score} puntos.")
print(f"La computadora obtuvo {computer_score} puntos.")
if user_score == computer_score:
    print("¡Empate!")
elif user_score > computer_score:
    print(f"¡{user_name} gana la partida!")
else:
    print("La computadora gana la partida.")
