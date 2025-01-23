# Diseña un programa que solicite al usuario una calificación entre 0 y 10. Luego, muestra si la calificación corresponde a "Aprobado" (>= 5) o "Suspenso" (< 5).

calificacion = int(input('Introduce una nota: '))

if calificacion >= 5:
    print('Aprobado')
else:
    print('Suspenso')