# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
n = int(input('Introduce un número entero : '))
for i in range(1, n + 1, 2):
    for j in range(i, 0, -2):
        print(j, end= '   ')
    print('')

