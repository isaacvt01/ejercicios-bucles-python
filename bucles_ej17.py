primero = 0
segundo = 0
while primero >= segundo:
    primero = input('introduce un num: ')
    primeroInt = int(primero)
    segundo = input('introduce otro num: ')
    segundoInt = int(segundo)


    if primeroInt > segundoInt:
        while primero > segundo:
            segundo = input('vuelve a introducir un numero: ')
            segundoInt = int(segundo)
    else:
        segundo = input('vuelve a introducir un numero: ')

num_primero = str(primero)
num_segundo = str(segundo)


print ('los números que has introducido son: ' + num_primero + ' y ' + num_segundo)