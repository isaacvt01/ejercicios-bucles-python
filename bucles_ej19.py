minimoNum = int(input('Escribe un número: '))
maximoNum = int(input('Escribe un número mayor que ' + str(minimoNum) + ':'))
listaDeNum = []
while maximoNum < minimoNum:
    maximoNum = int(input(str(maximoNum) + ' no es mayor que ' + str(minimoNum) + '. Vuelve a probar: '))
numeroDelMedio = int(input('Escribe un número entre ' + str(minimoNum) + ' y ' + str(maximoNum) + ': '))
listaDeNum.append(numeroDelMedio)
while numeroDelMedio < maximoNum and numeroDelMedio > minimoNum:
    numeroDelMedio = int(input('Escribe otro número entre ' + str(minimoNum) + ' y ' + str(maximoNum) + ': '))
    listaDeNum.append(numeroDelMedio)

s =','.join([str(i) for i in listaDeNum])
print (s)

