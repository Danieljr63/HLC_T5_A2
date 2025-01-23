# Escribe un programa que simule un sistema de contraseñas. Pide al usuario que ingrese una contraseña y verifica si coincide con una contraseña previamente definida (por ejemplo, "secreta123"). Si falla tres veces, muestra un mensaje de bloqueo.

def check_pass():
    system_password = "secreta123"
    tries = 0

    while tries < 3:
        user_password = input("Introduce tu contraseña")
        if system_password == user_password:
            print('Bienvenido')
            break
        else:
            tries += 1

check_pass()