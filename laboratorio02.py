
'''
2.	Deberá calcular la suma de los numeros 
pares comprendidos entre los 2 números ingresador por teclado. (5 puntos)
'''

#ingresar numeros
numero_uno = int(input("Ingresar el numero uno : "))
numero_dos = int(input("Ingresar el numero dos : "))

suma_total = 0

#suma nueros pares
for i in range(numero_uno + 1, numero_dos):

    if 0 == (i % 2):
        print ("Es par : ", i)
        suma_total = i + suma_total

if numero_uno != numero_dos:
   print ("suma total de numeros pares : ", suma_total)
else:
   print ("No existe numeros pares entre : ", numero_uno, "y", numero_dos) 



