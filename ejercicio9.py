#Escribe un programa que simule un juego de adivinanza. El programa debe generar un número aleatorio entre 1 y 50, y el usuario debe adivinarlo. Proporciona pistas como "Más alto" o "Más bajo" hasta que el usuario lo adivine correctamente.

import random

numero_random = random.randint(1, 50)
intentos = 0

while True:
    numero = int(input('Adivina el número (entre 1 y 50): '))
    intentos += 1
    if numero == numero_random:
        print('¡Correcto!')
        break
    elif numero < numero_random:
        print('Mas alto.')
    else:
        print('Mas bajo')