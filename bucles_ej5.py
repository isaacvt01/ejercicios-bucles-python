# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("¿Qué cantidad deseas invertir? "))
intereses = float(input('¿Intereses? '))
años = int(input('¿Años? '))
for i in range(años):
    cantidad *= 1 + intereses / 100
    #cantidad = cantidad * (1 + intereses / 100)
    print ('Capital tras ' +str(i+1) + 'años' + str(round(cantidad, 2)))
