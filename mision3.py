#Misión 3

opciones=0
paso1,paso2,paso3,paso4,paso5,paso6=False,False,False,False,False,False
datos=[[],[],[],[],[],[]]
sumas=[]
codigos=[]

while opciones !=13:
    opciones=int(input('''1. Digitar la cantidad de estudiantes a registrar.
2. Registrar los datos de los talentos.
3. Registrar nota de Misión 1.
4. Registrar nota de Misión 2.
5. Registrar nota de Misión 3.
6. Registrar nota de nivel final.
7. Nombre y nota del talento con la mejor nota de la misión 1.
8. Nombre y nota del talento con la mejor nota de la misión 2.
9. Nombre y nota del talento con la mejor nota de la misión 3.
10. Nombre y promedio de cada talento.
11. Código, nombre, nota Misión1, nota Misión2, nota Misión3 y prueba final.
12. Nombre de los desarrolladores.
13. Salir.
    Digita una opción: '''))

    match opciones:
        case 1:
            if paso1==False:
                cantidad=int(input('Digite la cantidad de estudiantes que desea registrar: '))
                print('')
                paso1=True
            else:
                print('')
                print('Ya hiciste este paso.')
                print('')

        case 2:
            if paso1==True and paso2==False:
                for n in range(cantidad):
                    nombre=str(input(f'Digite el nombre del talento N°{n+1}: '))
                    while nombre==" " or nombre=="":
                        print('El nombre es inválido, registrelo de nuevo.')
                        nombre=str(input(f'Digite el nombre del talento N°{n+1}: '))
                    else:
                        datos[0].append(nombre)
                    codigo=int(input(f'Digite el código del talento N°{n+1}: '))
                    while codigo in codigos:
                        print('El código no se puede repetir. Digite uno nuevo.')
                        codigo=int(input('Digite el nuevo código: '))
                    codigos.append(codigo)
                    datos[1].append(codigo)
                    print('')
                paso2=True
            else:
                print('No haz realizado el primer paso o ya hiciste este paso.')
                print('')

        case 3 :
            if paso1==True and paso2==True:
                for x in range(cantidad):
                    for a in datos[0]:
                        notaM1=int(input(f'Digite la nota de la Misión 1 de {a}: '))
                        while notaM1<0 or notaM1>100:
                            print('La nota es inválida. Registrela de nuevo.')
                            notaM1=int(input(f'Digite la nota de la Misión 1 de {a}: '))
                        else:
                            datos[2].append(notaM1)
                    print('')
                    break
                paso3=True
            else:
                print('Necesitas realizar el paso 1 y 2')
        
        case 4:
            if paso1==True and paso2==True:
                for x in range(cantidad):
                    for a in datos[0]:
                        notaM2=int(input(f'Digite la nota de la Misión 2 de {a}: '))
                        while notaM2<0 or notaM2>100:
                            print('La nota es inválida. Registrela de nuevo.')
                            notaM2=int(input(f'Digite la nota de la Misión 2 de {a}: '))
                        else:
                            datos[3].append(notaM2)
                    print('')                 
                    break
                paso4=True
            else:
                print('Necesitas realizar el paso 1 y 2')
        
        case 5:
            if paso1==True and paso2==True:
                for x in range(cantidad):
                    for a in datos[0]:
                        notaM3=int(input(f'Digite la nota de la Misión 3 de {a}: '))
                        while notaM3<0 or notaM3>100:
                            print('La nota es inválida. Registrela de nuevo.')
                            notaM3=int(input(f'Digite la nota de la Misión 3 de {a}: '))
                        else:
                            datos[4].append(notaM3)
                    print('')                 
                    break
                paso5=True
            else:
                print('Necesitas realizar el paso 1 y 2')
        
        case 6:
            if paso1==True and paso2==True:
                for x in range(cantidad):
                    for a in datos[0]:
                        notafinal=int(input(f'Digite la nota del nivel final de {a}: '))
                        while notafinal<0 or notafinal>100:
                            print('')
                            print('La nota es inválida. Registrela de nuevo.')
                            notafinal=int(input(f'Digite la nota del nivel final de {a}: '))
                        else:
                            datos[5].append(notafinal)
                    print('')                 
                    break
                paso6=True
            else:
                print('Necesitas realizar el paso 1 y 2')
        
        case 7:
            if paso1==True and paso2==True and paso3==True:
                mejor1=max(datos[2])
                for a,b in zip(datos[0],datos[2]):
                    if b == mejor1:
                        print('')
                        print(f'La mejor nota de la Misión 1 pertenece a {a} y es de {b}.')
                        print('')
            else:
                print('Necesitas realizar el paso 1, 2 y 3')
        
        case 8:
            if paso1==True and paso2==True and paso4==True:
                mejor2=max(datos[3])
                for a,b in zip(datos[0],datos[3]):
                    if b == mejor2:
                        print('')
                        print(f'La mejor nota de la Misión 2 pertenece a {a} y es de {b}.')
                        print('')
            else:
                print('Necesitas realizar el paso 1, 2 y 4')
        
        case 9:
            if paso1==True and paso2==True and paso5==True:
                mejor3=max(datos[4])
                for a,b in zip(datos[0],datos[4]):
                    if b == mejor3:
                        print('')
                        print(f'La mejor nota de la Misión 3 pertenece a {a} y es de {b}.')
                        print('')
            else:
                print('Necesitas realizar el paso 1, 2 y 5')

        case 10:
            if paso1==True and paso2==True and paso3==True and paso4==True and paso5==True and paso6==True:
                for co in range(cantidad):
                    suma2=0
                    for fi in range(2,6):
                        suma2+=datos[fi][co]
                    suma2=suma2/4
                    sumas.append(suma2)
                    for p,j in zip(datos[0],sumas):
                        print(f'El promedio de {p} es {j}')
            else:
                print('Te falta hacer alguno de los pasos anteriores')

        case 11:
            if paso1==True and paso2==True and paso3==True and paso4==True and paso5==True and paso6==True:
                for fila in range(len(datos)):
                    print('[',end='') 
                    for columna in range(len(datos[fila])):
                        if columna<len(datos[fila])-1: 
                            print(datos[fila][columna],end='\t ')
                        else:
                            print(datos[fila][columna],end='') 
                    print(']',end='')
                    print('')
                print(f'[{sumas}]')
            print('Te falta hacer alguno de los pasos anteriores')

        case 12:
            print('')
            print('REALIZADO POR MARIANA ACERO <3')
            print('')

        case 13:
            print('')
            print('Gracias por usar nuestro servicios')