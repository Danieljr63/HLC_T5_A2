# Escribe un programa que use un bucle para imprimir un triángulo de estrellas (★) basado en un número dado por el usuario. Por ejemplo, si el usuario ingresa 4:

# Ejemplo:
# Entrada del usuario: 4
# Salida:
# ★
# ★★
# ★★★
# ★★★★

numero = int(input('Introduce un número: '))
for i in range(1, numero + 1):
    print('★' * i)