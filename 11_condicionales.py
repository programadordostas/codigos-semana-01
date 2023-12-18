'''
Curso : Programacion Basica de Python
Sesion : 01 
Tema : Introduccion a Python - Condicionales
Fecha : 08/02/2020
Author : Jaime Gomez

'''

#####################################
#     Condicional : if
#####################################
'''
 El estudiante aprueba con 11, en 
 este caso se le envia su constancia
 virtual
'''
#'''

nota_final  = 11 # nota final

if nota_final >= 11:
    print("Envio de constancia virtual")

#'''

#####################################
#     Condicional : if ... else
#####################################
'''
 El estudiante aprueba con 11, en este caso se 
 le envia su constancia virtual. Si el estudiante 
 no aprueba solo se le envia su nota final.
'''

#'''

nota_final  = 10 # nota final

if nota_final >= 11:
    print("Envio de constancia virtual")
else:
    print("Envio de promedio final")

#'''


#####################################
#  Condicional : if .. elif .. else
#####################################
'''
 El estudiante aprueba con 11, en este caso se 
 le envia su constancia virtual. En caso el 
 estudiante tiene una nota entre 10 y menor a 11, 
 se le tomara una examen adicional, si el estudiante 
 tiene una nota menor a 10 solo se le  envia su nota final.
'''

#'''

nota_final  = 13 # nota final

if nota_final >= 11:
    print("Envio de constancia virtual")
elif nota_final < 11 and nota_final >= 10 :
    print("Se le toma examen de recuperacion")
else:
    print("Envio de promedio final")    

#'''



# Conditional expression

res =  "Jaime " if False else "Jose"
print( res)

res =  "Jaime " if True else "Jose"
print( res)


# Pass : To end an block
if True :
    pass

