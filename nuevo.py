#categoria=str(input('Digita tu categoria '))
#if categoria.lower()=='a':
#    print('Debes pagar',3000)
#elif categoria.lower()=='b':
#    print('Debes pagar',7000)
#elif categoria.lower()=='c':
#    print('Debes pagar',12000)
#else:
#    print('Debes pagar',21000)

######################################################################################################
#Pepejunior=int(input('Digita la edad de Pepe Junior '))
#Agripino=int(input('DIgita la edad de Agripino '))
#edad1=22


#if Pepejunior>Agripino and Pepejunior==edad1:
#    print('Pepe Junior es el mayor')
#elif Agripino>Pepejunior:
#    print('Agripino es el mayor')
#else:
#    print('No son los hijos de pepe')

######################################################################################################
#Salario=int(input('Digite el valor de su salario '))
#if Salario<=800000:
#    aumento=Salario*0.1
#    print('El valor de su aumento es ', aumento)
#    print('El valor de su salario es ', Salario + aumento)
#elif Salario>800000 and Salario<=1200000:
#    aumento=Salario*0.08
#    print('El valor de su aumento es ', aumento)
#    print('El valor de su salario es ', Salario + aumento)
#else:
#    aumento=Salario*0.05
#    print('El valor de su aumento es ', aumento)
#    print('El valor de su salario es ', Salario + aumento)

######################################################################################################
# salario=int(input('Digite el valor de su salario: '))
# Aux_trans=140606
# if salario<=2320000:
#     print('Tienes derecho al auxilio de transporte y tu salario será de: ', salario + Aux_trans)
# else:
#     print('No tienes derecho al auxilio de transporte y tu salario sigue siendo ', salario)

######################################################################################################
# val1=int(input('Digite el primer valor '))
# val2=int(input('Digite el segundo valor '))
# print('')
# operacion=int(input('''Escoge una opción:

# 1. suma
# 2. resta
# 3. multiplicación
# 4. división 
# ---- '''))

# match operacion:
#     case 1:
#         print(val1 + val2)
#     case 2:
#         print(val1 - val2)
#     case 3:
#         print(val1*val2)
#     case 4:
#         if val2==0:
#             print('No es posible dividir por cero')
#         else:
#             print(val1/val2)
#     case otro:
#         print('Error')

####################################################################################################

# numero=0
# residuo=0
# binario=''
# numero=int(input('Digita un numero: '))
# while numero>0:
#     residuo=numero%2
#     binario=str(residuo)+binario
#     numero=numero//2
# print(f'binario {binario}')

# i=1
# for i in range(20,10,-2):
#     print(i)

# num=0
# suma=0

# num=int(input('Digita un número: '))
# for x in range (num+2):
#     suma=suma+x
# print(f'La sumatoria es{suma}')

##########################################################################################

# numero=0
# if numero>=0 and numero<=9:
#     for x in range (1,11):
#         for i in range (1,11):
#             print(f'{x}x{i}={x*i}')
#         print('')
        
# else:
#     print('Ingrese el número de nuevo.')

# for m in range (1,10):
#     if m>6:
#         break
#     print(m)
#############################################################################

#valor=0
# while valor<500:
#     print(valor)
#     valor=valor+8

# for n in range (10,0,-1):
#     print(n)

# numero=10
# while numero>0:
#     print(numero)
#     numero=numero-1
#####################################################################

# num1=int(input('Digite el primer número: '))
# num2=int(input('Digite el segundo número: '))

# if num1>num2:
#     print('Digite los números del menor al mayor')
# else:
#     for n in range (num1,num2,1):
#         if n %2 ==0:
#             print(n)
#####################################################################

# num=0
# suma=0
# while num!=9999:
#     suma=suma+num
#     num=int(input('Digita un número: '))
# print(suma)
#############################################################################

# if suma>0:
#     print('El resultado es mayor a 0')
# elif suma<0:
# elif suma==0:
#     print('EL resultado es igual a 0')

# numE=int(input('Digita un número entero: '))
# maximo=-999999
# minimo=999999
# media=0
# contador=0
# while numE!=0:
#     if numE > maximo:
#         maximo=numE
#     if numE < minimo:
#         minimo=numE
#     media=media+numE
#     contador+=1
#     promedio=media/contador
#     numE=int(input('Digita un número entero: '))
# print(f'El número mayor es {maximo}')
# print(f'El número menor es {minimo}')
# print(f'El promedio es {promedio}')
############################################################################

# for n in range (1,101):
#     if n %2 ==0 and n %3 ==0:
#         print(n)

# num=0
# while num<100:
#     num+=1
#     if num %2 ==0 and num %3 ==0:
#         print(num)
##############################################################################

# contador=0
# for c in range (1,4,1):
#     c=int(input('Digita tu clave: \n'))
#     if c ==123456:
#         print('Contraseña correcta')
#         break
#     else:
#         contador=contador+1
#         if contador==3:
#             print('No tienes más intentos')
#             break
#         print(f'Contraseña incorrecta, llevas {contador} intentos')

# c=int(input('Ingresa tu contraseña: \n'))
# contador=1
# while c!=123456:
#     print(f'Contraseña incorrecta, llevas {contador} intentos.')
#     if contador==3:
#         print(f'No tienes más intentos')
#         break
#     c=int(input('Ingresa tu contraseña: \n'))
#     contador+=1
# if c==123456:
#     print(f'Contraseña correcta')

##########################################################################

# numero=0
# while numero<10:
#     numero+=1
#     print(numero)

#########################################################################
 
# for n in range (1,50):
#     numero=1
#     if numero % n==0:
#         numero+=1
#         print(numero)

# for n in range (1,101):
    # contador=0
    # for numero in range (1,n+1):
    #     if n % numero ==0:
    #         contador+=1
    # if contador==2:
    #     print(n)

# opciones=0
# acumulador=0
# promedio=0
# nota=0
# paso1=False
# paso2=False
# paso3=False
# paso4=False

# while opciones!=6:
#     opciones=int(input('''
# 1. Ingrese el nombre del estudiante: 
# 2. Ingrese las notas del estudiante: 
# 3. Mostrar la nota definitiva. 
# 4. Mostrar si aprobó o no la materia.
# 5. Mostrar el nombre del estudiante, la nota definitiva y si aparobó o no.
# 6. Salir.
# Digita una opción: '''))
#     match opciones:
#         case 1:
#             nombre=(input('Digite el nombre del estudiante: '))
#             paso1=True
#         case 2:
#             if paso1==True:
#                 for n in range(5):
#                     nota=-1
#                     while nota<0 or nota>5:
#                         nota=float(input(f'Digite la nota {n+1}: '))
#                     acumulador+=nota
#                     print('Gracias por tus notas')
#                     paso2=True
#             else:
#                 print('Debes hacer el paso 1.')
#         case 3:
#             if paso1==True and paso2==True:
#                 promedio=acumulador/5
#                 print(f'La nota definitiva es {promedio}.')
#                 paso3=True
#             else:
#                 print('Debes hacer el paso 1 y 2.')
#         case 4:
#             if paso1==True and paso2==True and paso3==True:
#                 if promedio<3.0:
#                     print(f'EL estudiante reprobó la materia con una nota de {promedio}.')
#                     resultado='reprobó'
#                 elif promedio>=3.0 and promedio<=5.0:
#                     print(f'El estudiante ha aprobado la materia con una nota de {promedio}.')
#                     resultado='aprobó'
#                     paso4=True
#                 else:
#                     ('Alguna nota fuera del rango.')
#         case 5:
#             if paso1==True and paso2==True and paso3==True and paso4==True:
#                 print(f'El nombre es: {nombre}, la definitiva es: {promedio} y {resultado}.')
#         case 6:
#             break
#         case otro:
#             print('Opción incorrecta')
            