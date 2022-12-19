lista = []
introducido = ' '
while introducido != 'Salir':
    introducido = input('Introduce un número random: ')
    if introducido != 'Salir':
        introducido = int(introducido)
        lista.append(introducido)
    else:
        continue

print('las palabras que has escrito son: ', lista)