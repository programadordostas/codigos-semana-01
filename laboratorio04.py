
'''

4.	Deberá calcular el promedio de los numero enteros 
comprendidos entre los 2 números ingresados por teclado. (5 puntos)

'''
#ingresar numeros
numero_uno = int(input("Ingresar el numero uno : "))
numero_dos = int(input("Ingresar el numero dos : "))

suma_total = 0
x = 0

#proemdio de numero entero
for i in range(numero_uno + 1, numero_dos):

    x += 1   
    suma_total = suma_total + i

promedio_total = suma_total / x
print ("promedio total . ", promedio_total)

