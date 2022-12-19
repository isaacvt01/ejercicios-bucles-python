lista = []
introducido = 0
while introducido < 10 and introducido >= 0:
    introducido = input('Introduce un número random: ')
    introducido = int(introducido)
    if introducido < 10 and introducido > 0:
        lista.append(introducido)
    else:
        continue

print('los números que has escrito son: ', lista)