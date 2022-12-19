# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input('Introduce una palabra: ')
indice = -1
for letra in palabra:
    print(palabra[indice])
    indice = indice - 1