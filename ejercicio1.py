# Crea un programa que pida al usuario su edad y determine si puede votar. Recuerda que para votar debe tener al menos 18 años.
edad = int(input('Ingrese su edad: '))
if edad <= 16:
    print('No puedes votar')
else:
    print('Puedes votar')