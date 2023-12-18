'''
3.	Deberá calcular la sumatoria  de los numeros 
impares elevados al cubo comprendidos entre los 2 números ingresador por teclado. (5 puntos)


    
'''
#ingresar numeros
numero_uno = int(input("Ingresar el numero uno : "))
numero_dos = int(input("Ingresar el numero dos : "))

suma_total = 0

#suma nueros impares
for i in range(numero_uno + 1, numero_dos):   
    
    if 0 != (i % 2):
        print ("numero impar", i)
        suma_total = i + suma_total
print("suma numeros impares:", suma_total)




