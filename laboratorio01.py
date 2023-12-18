'''
Curso : Programacion Basica de Python
Tarea : Laboratorio 01 
Fecha : 17/07/2023
Author : Enrique Sanchez

Laboratorio:
1.	Se deberá ingresar 2 número por consola , el primer dato ingresado 
será el menor valor (min_nro), el segundo dato ingresado será el mayor (max_nro). 
En caso no se cumpla esta condición debera volver a ingresar los dos números. (5 puntos)

'''

cond_uno = 1
cond_dos = 2

while cond_dos > cond_uno:
    # Solicita el ingreso de un dato
    min_nro = input("Ingresar el numero min_nro : ")
    max_nro = input("Ingresar el numero max_nro : ")

    if min_nro < max_nro:
        print ("Cumplio la condicion, donde el min_nro < max_nro")
        break
    else:
        print ("No cumplio la condicion, donde el min_nro < max_nro ")
        continue

