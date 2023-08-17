# MI INTENTO

from random import *

# nombre_usuario = input('Ingresa tu Nombre: ')
# print(f"Bueno, {nombre_usuario}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

# numero_random = randint(1, 100)

# intentos = 0
# numero_elegido = 0

# while intentos >= 8:
#     numero_elegido = int(input("Ingresa tu numero: "))
#     intentos -= 1
#     if (numero_elegido > 100 or numero_elegido < 1):
#         print("Has elegido un numero que no está permitido")
#         print(f'Te quedan {intentos} vidas')
#     elif (numero_elegido < numero_random):
#         print("Respuesta Incorrecta, has elegido un numero menor al número secreto")
#         print(f'Te quedan {intentos} vidas')
#     elif (numero_elegido > numero_random):
#         print("Respuesta Incorrecta, has elegido un numero mayor al numero secreto")
#         print(f'Te quedan {intentos} vidas')
#     elif (numero_elegido == numero_random):
#         print(
#             f"HAS GANADO, EL NUMERO ELEGIDO ES EL CORRECTO, TE TOMÓ {intentos} INTENTOS")
#         break

# else:
#     if intentos < 0:
#         print(f'el numero a adivinar era: {numero_random}')
#         print('Lo sentimos, agoto sus vidas, reinicie el juego')

# *INTENTO DEL PROFE

intentos = 0
numero_secreto = randint(1, 100)
estimado = 0
nombre = input("DIME TU NOMBRE: ")

print(f"Bueno {nombre}, he pensado un numero entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Ingresa tu numero: "))

    intentos += 1
    if (estimado not in range(1, 101)):
        print("Tu número no se encuentra en el rango que va de 1 a 100")
    elif estimado < numero_secreto:
        print("Mi numero es más alto")
    elif estimado > numero_secreto:
        print("Mi numero es más bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(
        f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")
