# Escribe un programa que pida al usuario una palabra y verifique si contiene alguna de las siguientes letras especiales: @, #, $, %. Si la palabra contiene al menos una, muestra un mensaje indicando cuál.

def check_chars()
    word = input('Introduce una palabra que contenga @, #, $, %: ')

    for char in word:
        if "@" == char:
            print("La palabra tiene el caracter @")
        if "#" == char:
            print("La palabra tiene el caracter #")
        if "$" == char:
            print("La palabra tiene el caracter $")
        if "%" == char:
            print("La palabra tiene el caracter %")

check_chars()