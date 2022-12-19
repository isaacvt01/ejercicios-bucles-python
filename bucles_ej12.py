# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input('Introduce una frase: ')
letra = input('Introduce una letra: ')
contadorRepeticiones = 0
for item in frase:
    if item == letra:
        contadorRepeticiones += 1
    else:
        continue
print (contadorRepeticiones)