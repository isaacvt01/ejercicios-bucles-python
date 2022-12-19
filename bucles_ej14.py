lista = []
introducido = ' '
while introducido != '':
    introducido = input('Introduce una palabra random: ')
    if introducido != '':
        lista.append(introducido)
    else:
        continue

print('las palabras que has escrito son: ', lista)
