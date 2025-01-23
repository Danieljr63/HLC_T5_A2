# Crea un programa que pida al usuario un número y determine si es par o impar utilizando un operador ternario.

numero = int(input('Introduce un número: '))

if numero % 2 == 0:
    print('El número ' + numero + ' es par')
else:
    print('El número ' + numero + ' es impar')