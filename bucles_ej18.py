listaNum = []
numero = int(input('Escribe un número: '))
listaNum.append(numero)
nuevoNum = int(input('Escribe un número mayor que: ' + str(numero) + ' '))
contador = 1
if nuevoNum > numero:
    listaNum.append(nuevoNum)
    while nuevoNum > listaNum[contador - 1]:
        nuevoNum = int(input('Escribe un número mayor que: ' + str(nuevoNum) + ' '))
        contador +=1
        if nuevoNum > listaNum[contador - 1]:
            listaNum.append(nuevoNum)
            numero = nuevoNum

else:
    s =','.join([str(i) for i in listaNum])



# for item in listaNum:
#     print (item)

s =','.join([str(i) for i in listaNum])
print (s)