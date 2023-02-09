# diccionario=[]


# nombresc=int(input('Digite el número de estudiantes a calcular: '))

# suma=0
# for x in range(nombresc):
#     suma=0
#     nombre=str(input(f'Digite el nombre de estudiante N°{x+1}: '))

#     genero=str(input(f'Digite el GÉNERO [F(femenino) o M(masculino)] del estudiante N°{x+1}: ')).lower()
#     while genero!='f' and genero!='m':
#         print('Digite el género correctamente.')
#         genero=str(input(f'Digite el GÉNERO [F(femenino) o M(masculino)] del estudiante N°{x+1}: ')).lower()
    
#     curso=int(input(f'Digite el CURSO del estudiante N°{x+1}: '))
#     while curso<1 or curso>11:
#         print('Digita el curso correctamente.')
#         curso=int(input(f'Digite el CURSO del estudiante N°{x+1}: '))

#     for i in range(3):
#         nota=float(input(f'Digite la nota final N°{i+1}: '))
#         while nota<0 or nota>5:
#             print('Digite la nota correctamente')
#             nota=float(input(f'Digite la nota final N°{i+1}: '))
#         else:
#             suma+=nota
#         prom=suma/3

#     if prom <3.5:
#         resultado="reprobado"
#     elif prom>=3.5:
#         resultado="Aprobado"
        
#     diccionario.append({
#         "nombre":nombre,
#         "genero":genero,
#         "curso":curso,
#         "notas": prom,
#         "resultado":resultado
#     })
# print(diccionario)

############################################################################################

# diccionario=[]

# empleados=int(input('Cuantos empleados son: '))
# valorhora=float(input('Digite el valor de la hora: '))

# for i in range(empleados):
#     nombre=str(input(f'Digite el nombre del empleado N°{i+1}: '))
#     antiguedad=int(input(f'Digite la antiguedad del empleado N°{i+1}: '))
#     horasc=int(input(f'Digite la cantidad de horas del empleado N°{i+1}: '))
#     print('')

#     importe=valorhora*horasc
#     años=antiguedad*30
#     suma=importe+años

#     descuentos=suma*0.13
#     total=suma-descuentos

#     diccionario.append({
#         "nombre":nombre,
#         "antiguedad":antiguedad,
#         "valor_hora":valorhora,
#         "total_bruto":suma,
#         "descuento":descuentos,
#         "total_a_cobrar":total
#     })
# print('')

# print(diccionario)

#############################################################################################

# plataforma=[]
# opciones=0
# promedios=[]
# nombres=[]
# codigos=[]
# paso1=False


# while opciones!=4:

#     opciones=int(input('''1. Digite los datos de los estudiantes.
# 2. Alumnos que aprobaron y que habilitan.
# 3. Código y nombre de los mejores promedios.
# 4. Salir.
# Digita una opción: '''))
#     match opciones:
#         case 1:
#             estudiantes=int(input('Digite el número de estudiantes: '))
#             for i in range(estudiantes):
#                 nombre=str(input(f'Digite el nombre del estudiante N°{i+1}: '))
#                 nombres.append(nombre)
#                 codigo=int(input(f'Digite el código del estudiante N°{i+1}: '))
#                 codigos.append(codigo)
#                 promedio=float(input(f'Digite el promedio del estudiante N°{i+1}: '))
#                 promedios.append(promedio)
#                 print('')
#                 paso1=True
#         case 2:
#             if paso1==True:
#                 for a,b in zip(nombres,promedios):
#                     if b>=7:
#                         print(f'{a} aprobó la materia con un promedio de {b}')
#                         print('')
#                     elif b<7 and b>=4:
#                         print(f'{a} reprobó la materia con un promedio de {b} y debe habiliatar en diciembre.')
#                         print('')
#                     elif b<4:
#                         print(f'{a} reprobó la materia con un promedio de {b} y debe habiliatar en marzo.')
#                         print('')
#         case 3:
#             if paso1==True:
#                 maximo=max(promedios)
#                 for a,b,c in zip(nombres,promedios,codigos):
#                     if b==maximo:
#                         print(f'{a} con el código: {c} tiene el mejor promedio de {maximo}')
        
#         case 4:
#             print('')
#             print('Hasta luego')

##########################################################################################################################

opciones=0
guardar=[]
codigos=[]
paso1,paso2=False,False

while opciones!=7:
    opciones=int(input('''1. Digite la cantidad de estudiantes.
2. Registre los datos de los estudiantes.
3. Mostrar listado de estudiantes.
4. Registrar notas estudiantes.
5. Imprimir notas estudiantes.
6. Acerca del autor.
7. Salir
Digita una opción: '''))

    match opciones:
        case 1:
            cantidad=(int(input('Digite la cantidad de estudiantes a registrar: ')))
            print('')
            paso1=True
        
        case 2:
            if paso1==True:
                for a in range(cantidad):
                    name=str(input(f'Digita el nombre del estudiante N°{a+1}: '))
                    codigo=int(input(f'Digita el código del estudiante N°{a+1}: '))
                    while codigo in codigos:
                        print('El código no se puede repetir. Digite uno nuevo.')
                        codigo=int(input('Digite el nuevo código: '))
                    codigos.append(codigo)
                    nivel=int(input(f'Elija el nivel del estudiante N°{a+1}: 1.Begginer\n2.Junior\n3.Senior\nDigite una opción: '))
                    print('')

                    guardar.append({
                        "nombre":name,
                        "codigo":codigo,
                        "nivel":nivel
                    })
                    paso2=True
        
        case 3:
            if paso1==True and paso2==True:
                for i in guardar:
                    print(i)
                print('')

        case 4:
            if paso1==True and paso2==True:
                for x in guardar:
                    for a in range(3):
                        notas=int(input(f'Digite la nota N°{a+1} de {x["nombre"]} con el código {x["codigo"]}: '))
                        while notas<0 or notas>5:
                            notas=int(input(f'Digite correctamente la nota N°{a+1} de {x["nombre"]} con el código {x["codigo"]}: '))
                        
