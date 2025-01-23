# Crea un programa que genere los primeros 10 números de la serie de Fibonacci y los imprima.

def fibonacci():
    a = 0
    b = 1

    for i in range(10):
        print(a)
        a, b = b, a+b
fibonacci()