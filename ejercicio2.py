# Escribe un programa que pida al usuario tres números y determine cuál es el mayor. Si hay un empate entre dos o más números, indícalo también.

numero = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese un numero: '))
numero3 = int(input('Ingrese un numero: '))

if numero > numero2 and numero > numero3:
    print('El primer numero es el mayor')
elif numero2 > numero and numero2 > numero3:
    print('El segundo numero es el mayor')
elif numero3 > numero and numero3 > numero2:
    print('El tercer numero es el mayor')
elif numero == numero2 or numero == numero3 and numero2 == numero or numero2 == numero3 and numero3 == numero or numero3 == numero2:
    print('Hay empate')