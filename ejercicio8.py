numero = int(input('Introduce un numero positivo: '))

# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(numero)]
print(cuadrados)