#Diseñar un algoritmo que lea 10 números y los guarde en un vector

# lista=[]
# for n in range(10):
#     lista.append(int(input('Digita un número: ')))
# print(lista)

# suma=13
# def sumar(num1,num2):
#     suma=num1+num2
#     print(suma)

# sumar(10,3)
# print(suma)


# lista=[1,6,8,1,3,6,4,5,2,6]
# lista2=['a','b','c','d']
# lista.extend(lista2)
# print(lista)

#############################################################

# import random
# lista=[]
# for n in range (1,11):
#     num=(random.randint(1,10))
#     lista.append(int(num))
# print(lista)
# suma=sum(lista)
# print(f'La suma es: {suma}')

#############################################################

# lista=[10,0,3,61,9,20,17,8,2,1]
# max=lista[0]
# for m in (lista):
#     if m > max:
#         max=m
# print(f'El número mayor es: {max}.')

# lista=[10,0,3,61,9,20,17,8,2,1]
# men=lista[0]
# for n in (lista):
#     if n < men:
#         men=n
# print(f'El número menor es: {men}.')

# lista=[10,0,3,61,9,20,17,8,2,1]
# max=lista[0]
# for m in range (10):
#     if lista[m] > max:
#         max=lista[m]
# print(f'El número mayor es: {max}.')

# lista=[10,0,3,61,9,20,17,8,2,1]
# lista.sort()
# print(lista)
# mayor=max(lista)
# print(mayor)

# lista=[10,0,3,61,9,20,17,8,2,1]
# lista.insert(-4,5)
# print(lista)

# lista=[10,0,3,61,3,20,17,8,2,1]
# lista.reverse()
# print(lista)

########################################################

# menu=0
# nombres=[]
# notas=[]
# paso1,paso2,paso3,paso4=False,False,False,False

# while menu !=5:
#     menu=int(input('''1. Nombre de los 5 estudiantes: 
# 2. Nota de cada estudiante: 
# 3. Mayor nota y a quien le pertenece: 
# 4. Visualizar estudiantes y sus notas: 
# 5. Salir
# Digita una opción: '''))

#     match menu:
#         case 1:
#             for e in range (5):
#                 nombre=str(input('Digite el nombre del estudiante: '))
#                 nombres.append(nombre)
#             print('')
#             paso1=True
#         case 2:
#             if paso1==True:
#                 for n in (nombres):
#                     nota=float(input(f'Digite la nota de {n}: '))
#                     if nota >=0 and nota<=5.0:
#                         notas.append(nota)
#                     else:
#                         print('Digite correctamente la nota.')
#                         print('')
#                 paso2=True
#         case 3:
#             if paso1==True and paso2==True:
#                 mayor=notas[0]
#                 for x in range(5):
#                     if notas[x]>mayor:
#                         mayor=notas[x]
#                 for m,t in zip(nombres,notas):
#                     if t == mayor:
#                         print(f'La mayor nota le pertenece a {m}, y es de {mayor}')
#                         print('')
#         case 4:
#             if paso1==True and paso2==True:
#                 for m,t in zip(nombres,notas):
#                     print('')
#                     print(m,t)
#                     print('')
#         case 5:
#             print('')
#             print('Gracias por usar nuestro servicio.')
#             print('')
#         case otro:
#             print('registra un número correcto del menú.')

####################################################################

# opciones=0
# animales=[]
# paso1=False

# while opciones !=5:
#     opciones=int(input('''1.Digite los animales de la lista. 
# 2. Animales ordenados alfabéticamente. 
# 3. Animales dentro de la lista. 
# 4. Escribe un animal y verifica si está en la lista. 
# 5. Salir. 
# Digita una opción: '''))

#     match opciones:
#         case 1:
#             for a in range(1,11):
#                 animal=str(input(f'Digite el nombre del animal N°{a}: '))
#                 animal=animal.capitalize()
#                 animales.append(animal)
#             print('')
#             paso1=True
#         case 2:
#             if paso1==True:
#                 animales.sort()
#                 print(animales)
#             print('')
#             paso2=True
#         case 3:
#             if paso1==True:
#                 num=int(input('Digite un número del 1 al 10: '))
#                 if num >=1 and num <=10:
#                         print(animales[num-1:10])
#                 else:
#                     print('Digita un número dentro del rango (1-10).')
#         case 4:
#             if paso1==True:
#                 name=str(input('Digite el animal que deseas verificar: '))
#                 name=name.capitalize()
#                 if name in animales:
#                     print(f'{name} se encuentra dentro de la lista.')
#                     print('')
#                 else:
#                     print(f'{name} no se encuentra dentro de la lista')
#                     print('')
#         case 5:
#             print('Gracias por usar nuestro servicio.')

#######################################################################################

# arreglo=[1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2,7]
# repetidos=[]
# contador=0
# numero=int(input('Digita un número del 1 al 10: '))

# if numero in arreglo:
#     cont=arreglo.count(numero)
#     psc=arreglo.index(numero)
#     if cont>1:
#         for m in arreglo:
#             if m==numero:
#                 repetidos.append(contador)
#             contador+=1
#         print(f'El número se encuentra en la posición {repetidos}')
#     else:
#         print(f'EL número solo se encuentra en la posición {psc}')

########################################################################################

# numeros=[33,55,77,81,48]
# suma=sum(numeros)
# print(f'{numeros} = {suma}')

# suma=0
# numeros=[33,55,77,81,48]
# for s in (numeros):
#     suma+=s
# #    print(f'{s}+')
#     print(f'{s} +', end =' ')
# print(f'= {suma}')

########################################################################################

# usuario=['pepito89','supermangui','esparnancacion']
# contraseñas=['123456','password','qwerty123']
# cont=0
# lug=0
# oportunidades=3
# usert=False
# passwt=False

# while usert==False or passwt==False:
#     user=str(input('Digite su usuario: '))
#     password=str(input('Digite su contraseña: '))
#     user=user.lower()

#     for u in (usuario):
#         if user==u:
#             usert=True
#             lug=user.index(u)
#     cont=0
#     for c in (contraseñas):
#         if password==c and lug==cont:
#             passwt=True
#         cont+=1

#     if usert==True and passwt==True:
#         print('Bienvenido')
#         break
#     else:
#         print('Intentalo de nuevo')
#         oportunidades+=1
#         if oportunidades==3:
#             print('No tienes más intentos')

#########################################################################################

# matriz=[]
# lista1=[]
# lista2=[]
# lista3=[]
# lista4=[]
# lista5=[]
# for a in range (1,11):
#     lista1.append(a)
# for b in range (11,21):
#     lista2.append(b)
# for c in range (21,31):
#     lista3.append(c)
# for d in range (31,41):
#     lista4.append(d)
# for e in range (41,51):
#     lista5.append(e)

# print(lista1)
# print(lista2)
# print(lista3)
# print(lista4)
# print(lista5)

##############################################################################################

# matriz=[]
# sumacol=[]
# sumafila=[]

# for fila in range (4):
#     matriz.append([])
#     for columna in range (6):
#         matriz[fila].append(columna+1+(fila*6))
        
# for fila in range(len(matriz)):
#     print('[',end='') 
#     for columna in range(len(matriz[fila])):
#         if columna<len(matriz[fila])-1: 
#             print(matriz[fila][columna],end='\t ')
#         else:
#            print(matriz[fila][columna],end='') 
#     print(']',end='')
#     print('')

# for f in range(4):
#     suma=0
#     for c in range (6):
#         suma+=matriz[fila][columna]
#         sumafila.append(suma)

# for c in range(6):
#     suma2=0
#     for f in range(4):
#         sumacol.append(suma2)
#         suma2+=matriz[columna][fila]

########################################################################################

# nombres=[]
# lista=0
# cantidad=int(input('Cuantas personas vas a digitar?: '))

# while lista<cantidad:
#     nombre=(input('Digite la lista de nombres: '))
#     nombres.append(nombre)
#     lista+=1

# nombresA=nombres.copy()
# nombresA.sort()
# print(f'Tu lista fue: {nombres}')
# print('')
# print(f'Tu lista en orden alfabético es: {nombresA}')

##########################################################################################

# lista1=[2,4,6,8,10,12,14,16,18,4]
# lista2=[2,3,6,9,12,15,4,18,2]

# for a in lista1:
#     for b in lista2:
#         if a == b:
#             break
#     if a!=b:
#         print(a)

#############################################################################################

# Bogota=[19,19,17,18,20]
# Bucaramanga=[27,26,26,26,27]
# Medellin=[27,26,26,27,29]
# ciudades=[Bogota,Bucaramanga,Medellin]
# nombres=('Bogota','Bucaramanga','Medellin')

# cont=0
# for i in ciudades:
#     maximo=max(i)
#     print(f'La temperatura máxima de {nombres[cont]} es {maximo}')
#     minimo=min(i)
#     print(f'La temperatura mínima de {nombres[cont]} es {minimo}')
#     prom=sum(i)/len(i)
#     print(f'La temperatura promedio de {nombres[cont]} es: {prom}')
#     print('')
#     cont+=1

################################################################################################

Todo=[[],[],[],[],[],[],[],[]]

nombresT=int(input('Digite el número de estudiantes a calcular: '))

for i in range(nombresT):
    nombre=str(input(f'Digite el NOMBRE del estudiante N°{i+1}: '))
    Todo[0].append(nombre)

    genero=str(input(f'Digite el GÉNERO [F(femenino) o M(masculino)] del estudiante N°{i+1}: ')).lower()
    while genero!='f' and genero!='m':
        print('Digite el género correctamente.')
        genero=str(input(f'Digite el GÉNERO [F(femenino) o M(masculino)] del estudiante N°{i+1}: ')).lower()
    else:
        Todo[1].append(genero)

    curso=int(input(f'Digite el CURSO del estudiante N°{i+1}: '))
    while curso<1 or curso>11:
        print('Digita el curso correctamente.')
        curso=int(input(f'Digite el CURSO del estudiante N°{i+1}: '))
    else:
        Todo[2].append(curso)

for x in Todo[0]:
    notam=float(input(f'Digite la nota final de matematicas de {x}: '))
    while notam<0 or notam>5:
        print('Digite la nota correctamente')
        notam=float(input(f'Digite la nota final de matematicas de {x}: '))
    else:
        Todo[3].append(notam)

    notai=float(input(f'Digite la nota final de inglés de {x}: '))
    while notai<0 or notai>5:
        print('Digite la nota correctamente')
        notai=float(input(f'Digite la nota final de inglés de {x}: '))
    else:
        Todo[4].append(notai)

    notaq=float(input(f'Digite la nota final de química de {x}: '))
    while notaq<0 or notaq>5:
        print('Digite la nota correctamente')
        notaq=float(input(f'Digite la nota final de química de {x}: '))
    else:
        Todo[5].append(notaq)

for co in range(nombresT):
    suma2=0
    for fi in range(3,6):
        suma2+=Todo[fi][co]
    suma2=suma2/3
    Todo[6].append(suma2)

for m in Todo[6]:
    if m>=3.5:
        Todo[7].append('Aprobó')
    else:
        Todo[7].append('reprobó')

for fila in range(len(Todo)):
    print('[',end='') 
    for columna in range(len(Todo[fila])):
        if columna<len(Todo[fila])-1: 
            print(Todo[fila][columna],end='\t ')
        else:
            print(Todo[fila][columna],end='') 
    print(']',end='') 
    print('')

################################################################################################################

# diccionario= {
#     "nombreE" : "",
#     "GeneroE" : "",
#     "Curso" : "",
#     "Notas" : "",
#     "Promedio" : "",
#     "Aprobó?" : ""
# }

# print(diccionario)

# for fila in range(len(datos)):
#                 print('[',end='') 
#             for columna in range(len(datos[fila])):
#                 if columna<len(datos[fila])-1: 
#                     print(datos[fila][columna],end='\t ')
#                 else:
#                     print(datos[fila][columna],end='') 
#             print(']',end='') 
#             print('')
