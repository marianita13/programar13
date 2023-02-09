#EJERCICIO DE ESTRUCTURA CÍCLICA (BUCLES)

#Ejercicio 1

# numero=1
# contador=0
# print('La suma termina cuando digitas el 0')
# while numero>0:
#     numero=float(input('Digite los números: '))
#     contador+=numero
# print('')
# print(f'La suma total es {contador}')

#################################################################
#Ejercicio 2

# import random
# num=1
# while num!=0:
#     num=(random.randint(0,10))
#     print(num)

###############################################################
#Ejercicio 3

# import random
# for n in range (1,21):
#     print(random.randint (1,1001))

###############################################################
#Ejercicio 4

# numero=int(input('Digite un número: '))
# contador=0
# for i in range (numero):
#     contador+=1
#     if contador %2 == 1:
#         print(contador)

#############################################################
#Ejercicio 5

# muestreo=0
# contadorn=0
# contadorj=0
# contadorad=0
# contadorab=0
# muestreo=int(input('Digite el número de personas del muestreo: '))
# while muestreo==20:
#     niños=int(input('Cuantos niños participan?: '))
#     jóvenes=int(input('Cuantos jóvenes participan?: '))
#     adultos=int(input('Cuantos adultos participan?: '))
#     abuelos=int(input('Cuantos abuelos participan?: '))
#     if niños+jóvenes+adultos+abuelos==20:
#         for niños in range (1,niños+1):
#            pniño=float(input(f'Digite el peso del niño {niños}: '))
#            contadorn+=pniño
#            print('')
#            for jóvenes in range (1,jóvenes+1):
#             pjoven=float(input(f'Digite el peso del jóven {jóvenes}: '))
#             contadorj+=pjoven
#         print('')
#         for adultos in range (1, adultos+1):    
#            padulto=float(input(f'Digite el peso del adulto {adultos}: '))
#            contadorad+=padulto
#         print('')
#         for abuelos in range (1,abuelos+1):
#            pabuelo=float(input(f'Digite el peso del adulto mayor {abuelos}: '))
#            contadorab+=pabuelo
#         print('')
#         promn=contadorn/niños
#         print(f'El peso promedio de los niños es: {promn}')

#         promj=contadorj/jóvenes
#         print(f'El peso promedio de los jóvenes es: {promj}')

#         promad=contadorad/adultos
#         print(f'El peso promedio de los adultos es: {promad}')

#         promab=contadorab/abuelos
#         print(f'El peso promedio de los adultos mayores es: {promab}')
#         break
#     else:
#        print('Digite el número correcto del muestreo.')
# print('Digite el número correcto') 

####################################################################################3
#Otra versión del ejercicio 5

# muestreo=0
# contadorn=0
# contadorj=0
# contadorad=0
# contadorab=0
# contadorpn=0
# contadorpj=0
# contadorpad=0
# contadorpab=0
# muestreo=int(input('Digite el número de personas del muestreo: '))
# while muestreo == 20:
#     categoria=int(input('Digite su edad: '))
#     if categoria>=0 and categoria<=12:
#         contadorn+=1
#     if categoria>=13 and categoria<=29:
#         contadorj+=1
#     if categoria>=30 and categoria<=59:
#         contadorad+=1
#     if categoria>=60:
#         contadorab+=1
#     if contadorab+contadorad+contadorn+contadorj == 20:
#         print(f'Hay {contadorn} niños')
#         print(f'Hay {contadorj} jóvenes')
#         print(f'Hay {contadorad} adultos')
#         print(f'Hay {contadorab} mayores de edad')
#         for niños in range (1,contadorn+1):
#            pniño=float(input(f'Digite el peso del niño {niños}: '))
#            contadorpn+=pniño
#         print('')
#         for jóvenes in range (1,contadorj+1):
#             pjoven=float(input(f'Digite el peso del jóven {jóvenes}: '))
#             contadorpj+=pjoven
#         print('')
#         for adultos in range (1, contadorad+1):    
#            padulto=float(input(f'Digite el peso del adulto {adultos}: '))
#            contadorpad+=padulto
#         print('')
#         for abuelos in range (1,contadorab+1):
#            pabuelo=float(input(f'Digite el peso del adulto mayor {abuelos}: '))
#            contadorpab+=pabuelo
#         print('')
#         promn=contadorpn/contadorn
#         print(f'El peso promedio de los niños es: {promn}')

#         promj=contadorpj/contadorj
#         print(f'El peso promedio de los jóvenes es: {promj}')

#         promad=contadorpad/contadorad
#         print(f'El peso promedio de los adultos es: {promad}')

#         promab=contadorpab/contadorab
#         print(f'El peso promedio de los adultos mayores es: {promab}')
#         break
# print('Digite el número correcto del muestreo.') 

######################################################################################
#Ejercicio 6

# for a in range (1,2):
#     for b in range (1,6):
#         for c in range (1,5):
#             if c != 4:
#                 print(a,b,c, end= ' - ')
#             else:
#                 print(a,b,c, end='')
#         print('')

###########################################################################
#Ejercicio 7

# animales=int(input('''1. Elefantes
# 2. Jirafas
# 3. Chimpacés
# Escoja el animal a estudiar: '''))

# match animales:
#     case 1:
#         contE=0
#         edadE1=0
#         edadE2=0
#         edadE3=0
#         while contE<20:
#             edad=float(input('Digite la edad de los elefantes: '))
#             contE+=1
#             if edad>0 and edad<=1:
#                 edadE1+=1
#             elif edad>1 and edad<3:
#                 edadE2+=1
#             elif edad>=3:
#                 edadE3+=1
#         por1=(edadE1/contE)*100
#         por2=(edadE2/contE)*100
#         por3=(edadE3/contE)*100
#         print(f'De 0 a 1 año hay un {por1}% de elefantes,\nentre 1 a menos de 3 años hay un {por2}% de elefantes,\nY mayores a 3 años hay un {por3}% de elefantes')
#     case 2:
#         contJ=0
#         edadJ1=0
#         edadJ2=0
#         edadJ3=0
#         while contJ<15:
#             edad=float(input('Digite la edad de las jirafas: '))
#             contJ+=1
#             if edad>0 and edad<=1:
#                 edadJ1+=1
#             elif edad>1 and edad<3:
#                 edadJ2+=1
#             elif edad>=3:
#                 edadJ3+=1
#         por1=(edadJ1/contJ)*100
#         por2=(edadJ2/contJ)*100
#         por3=(edadJ3/contJ)*100
#         print(f'De 0 a 1 año hay un {por1}% de jirafas,\nentre 1 a menos de 3 años hay un {por2}% de jirafas,\nY mayores a 3 años hay un {por3}% de jirafas')
#     case 3:
#         contC=0
#         edadC1=0
#         edadC2=0
#         edadC3=0
#         while contC<40:
#             edad=float(input('Digite la edad de los chimpacés: '))
#             contC+=1
#             if edad>0 and edad<=1:
#                 edadC1+=1
#             elif edad>1 and edad<3:
#                 edadC2+=1
#             elif edad>=3:
#                 edadC3+=1
#         por1=(edadC1/contC)*100
#         por2=(edadC2/contC)*100
#         por3=(edadC3/contC)*100
#         print(f'De 0 a 1 año hay un {por1}% de chimpancés,\nentre 1 a menos de 3 años hay un {por2}% de chimpancés,\nY mayores a 3 años hay un {por3}% de chimpancés')

##########################################################################################################
#Ejercicio 8

# vendedores=int(input('Digite el número de vendedores: '))
# sueldo=float(input('Digite el sueldo base: '))
# for v in range (vendedores):
#     venta1=float(input(f'Digite el valor de la primera venta: '))
#     venta2=float(input(f'Digite el valor de la segunda venta: '))
#     venta3=float(input(f'Digite el valor de la tercera venta: '))
#     print('')
#     comisión=(venta1+venta2+venta3)*0.1
#     total=sueldo+comisión
#     print(f'El vendedor hizo 3 ventas por valor de {venta1}, {venta2} y {venta3} pesos y recibirá un pago total de {total} pesos.')
#     print('')

##################################################################################################################
#Ejercicio 9

# autos=int(input('Digite el número de autos vendidos: '))
# cont=0
# comision=0
# ventas=0
# for v in range (autos):
#     cont+=1
#     valor=float(input(f'Digite el valor del auto {cont}: '))
#     comision+=170000
#     ventas+=valor
#     extra=ventas*0.05
# print(f'Por un total de {autos} autos, con un total de ventas de {ventas}, y con una comisión de {comision} y un extra del 5% de {extra}\nSu sueldo total es de {950000+comision+extra}')

####################################################################################################
#Ejercicio 10

# nombre=str(input('Digita tu nombre: '))
# print('Las 2 primeras notas valen 40% y las otras 3 valen 60%')
# cont=0
# suma1=0
# suma2=0
# for n in range(1,6):
#     cont+=1
#     nota=float(input('Digite su nota: '))
#     if cont<=2:
#         suma1+=nota
#     elif cont>2:
#         suma2+=nota
# porcentaje=(suma1/2)*0.4+(suma2/3)*0.6
# print('')
# print(f'El estudiante {nombre} ha sacado un promedio de {porcentaje}')
