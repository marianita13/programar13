# factura=int(input('Digita el valor de tu factura '))
# print('')
# estrato=int(input('''1. Estrato 1
# 2. Estrato 2
# 3. Estrato 3
# 4. Estrato 4

# Selecciona tu estrato: '''))

# match estrato:
#     case 1:
#         subsidio=factura*0.1
#         print('Su subsidio es del 10% y el total a pagar es ', (factura-subsidio))
#     case 2:
#         subsidio=factura*0.08
#         print('Su subsidio es del 8% y el total a pagar es ', (factura-subsidio))
#     case 3:
#         subsidio=factura*0.06
#         print('Su subsidio es del 6% y el total a pagar es ', (factura-subsidio))
#     case 4:
#         subsidio=factura*0.04
#         print('Su subsidio es del 4% y el total a pagar es ', (factura-subsidio))
#     case _:
#         print('No tiene derecho al subsidio')

#####################################################################################################

# camisas=int(input('Digite el numero de camisas que compró: '))
# print('')
# Precio=float(input('Digite el pago total por las camisas: '))
# print('')

# if camisas>=1000:
#     descuento=camisas*0.1
# elif camisas>=500 and camisas<=999:
#     descuento=camisas*0.08
# elif camisas>=200 and camisas<=499:
#     descuento=camisas*0.05
# else:
#     descuento=0
# print(f'''En nuestra tiendas haz llevado un total de {camisas} camisas, por un total de {Precio} pesos. 
# Por llevar en grandes cantidades, te damos un descuento del {descuento}%. EL valor unitario de cada camisa es:
# {Precio/camisas} y el total a pagar es de: {Precio-(Precio*descuento)}''')

################################################################################################################

# deposito=int(input('Digite el periodo de tiempo de su depósito '))
# valor=float(input('DIgite el valor de su depósito '))

# if deposito<=6:
#     tasa=(valor*0.08)/12
#     interes=tasa*deposito
# elif deposito>7:
#     tasa=(valor*0.1)/12
#     interes=tasa*deposito
# elif deposito>13:
#     tasa=(valor*0.12)/12
#     interes=tasa*deposito
# elif deposito>19:
#     tasa=(valor*0.15)/12
#     interes=tasa*deposito
# elif deposito>24:
#     tasa=(valor*0.18)/12
#     interes=tasa*deposito

# print('El valor total de su ganancia mensual será de ',(tasa), 'dolares')
# print('Su ganancia total es de ',(interes),'dolares')
# print('El saldo total de su deposito es de:', (valor+interes), 'dolares')

################################################################################################################

# Cargo=int(input('''1. Vendedores
# 2. Diseñadores
# 3. Administrativos 
# Seleccione su cargo: '''))
# print('')
# Sueldo=float(input('Digite su salario '))

# match Cargo:
#     case 1:
#         aumento=Sueldo*0.12
#     case 2:
#         aumento=Sueldo*0.1
#     case 3:
#         aumento=Sueldo*0.05
#     case _:
#         aumento=0
# print('El aumento de su salario será de',(aumento),'Y su salario total será de ',(Sueldo+aumento),'pesos')

#######################################################################################################

# ventas=int(input('Digite el valor total de las ventas durante el mes '))
# Salario=int(input('Digite el valor de su salario '))

# if ventas>=1000000 and ventas<=2000000:
#     bonificación=3
# elif ventas>2000000 and ventas<=5000000:
#     bonificación=5
# elif ventas>5000000:
#     bonificación=8
# else:
#     bonificación=0
# Tbon=(ventas*bonificación)/100
# Salariototal=Salario+Tbon

# print('El valor de su comisión es del',(bonificación),'%, con un total de ',(Tbon),' pesos, y el saldo total es de',(Salariototal),'pesos.')

#######################################################################################################################

# num1=int(input(''' Recordar que los números deben ser distintos: 

# Digite el primer número '''))
# num2=int(input('Digite el segundo número '))
# num3=int(input('Digite el tercer número '))

# if num1!=num2 and num1!=num3 and num2!=num3:
#     if num1>num2 and num1>num3:
#         print(f'El número mayor es {num1}')
#     elif num2>num1 and num2>num3:
#         print(f'El número mayor es {num2}')
#     elif num3>num1 and num3>num2:
#         print(f'El número mayor es {num3}')
#     else:
#         print('Error')
# else:
#     print('Todos los números deben ser diferentes ')

###########################################################################################################

# nota1=float(input('Digite la primer nota '))
# nota2=float(input('Digite la segunda nota '))
# nota3=float(input('Digite la tercera nota '))

# if nota1>0 and nota1<=5 and nota2>0 and nota2<=5 and nota3>0 and nota3<=5:
#     NotaD=(nota1+nota2+nota3)/3
#     if NotaD>=3.0:
#         print('EL estudiante ha aprobado la materia')
#     else:
#         print('El estudiante no ha aprobado la materia')
# else:
#     print('Existe una nota fuera del rango establecido')

###############################################################################################################

# Num1=int(input('Digite el primer número '))
# Num2=int(input('Digite el segundo número '))

# if Num1 % Num2 ==0 or Num2 % Num1 ==0:
#     print('Son múltiplos')
# else:
#     print('No son múltiplos')

#####################################################################

# parcial1=float(input('Digite la nota del primer parcial '))
# parcial2=float(input('Digite la nota del segundo parcial '))

# pp1_2=float(parcial1+parcial2)/2
# if parcial1>=0 and parcial1<=5 and parcial2>=0 and parcial2<=5:
#     if pp1_2>=2.0:
#         examenfinal=float(input('Digite la nota del examen final '))
#         if examenfinal>2.0:
#             pp=(parcial1*0.3)+(parcial2*0.3)+(examenfinal*0.4)
#             notad=(pp)
#             if notad>=3.0:
#                 print(f'EL estudiante aprueba la materia con una nota definitiva de {notad}')
#             elif  notad<3.0:
#                 if examenfinal>2.0:
#                     print('Puede habilitar')
#                     habilitación=float(input('Digite la nota de la habilitación '))
#                     print(f'Su nota definitiva es {habilitación}')
#                 else:
#                     print('No puede habilitar')
#         elif examenfinal<2.0:
#             print(f'Su nota definitiva es {examenfinal}')
#     elif pp1_2<2.0:
#         print(f'No puede presentar el examen final y su definitiva es {pp1_2}')
# else:
#     print('Notas fuera del rango')

###########################################################################################

# num1=int(input('Digite el primer número '))
# num2=int(input('Digite el segundo número '))
# num3=int(input('Digite el tercer número '))

# if (num1>num2) and (num1>num3) and (num2>num3):
#     print(f'Los números de menor a mayor son:\n{num3}\n{num2}\n{num1}')
# elif (num1>num2) and (num1>num3) and (num3>num2):
#     print(f'Los números de menor a mayor son:\n{num2}\n{num3}\n{num1}')
# elif (num2>num1) and (num2>num3) and (num1>num3):
#     print(f'Los números de menor a mayor son:\n{num3}\n{num1}\n{num2}')
# elif (num2>num1) and (num2>num3) and (num3>num1):
#     print(f'Los números de menor a mayor son:\n{num1}\n{num3}\n{num2}')
# elif (num3>num1) and (num3>num2) and (num1>num2):
#     print(f'Los números de menor a mayor son:\n{num2}\n{num1}\n{num3}')
# elif (num3>num1) and (num3>num2) and (num2>num3):
#     print(f'Los números de menor a mayor son:\n{num1}\n{num2}\n{num3}')
# else:
#     print('Todos los números deben ser diferentes')

##############################################################################################

# Salario=int(input('Digite el valor de su salario: '))
# solteros=int(input('''Es usted soltero? 
# 1. Si
# 2. NO 
# '''))

# match solteros:
#     case 1:
#         tiempo=int(input('Digite cuantos años ha trabajado en la empresa: '))
#         if tiempo>0 and tiempo<=5:
#             bonificación=Salario*0.02
#         elif tiempo>=6 and tiempo<=10:
#             bonificación=Salario*0.05
#         elif tiempo>=11:
#             bonificación=Salario*0.1

#     case 2:
#         tiempo=int(input('Digite cuantos años ha trabajado en la empresa: '))
#         if tiempo>0 and tiempo<=5:
#             bonificación=Salario*0.05
#         elif tiempo>=6 and tiempo<=10:
#             bonificación=Salario*0.1
#         elif tiempo>=11:
#             bonificación=Salario*0.15
# print(f'Usted recibirá una bonificación de {bonificación} y un salario total de {Salario+bonificación} pesos.')

######################################################################################################################

# años=int(input('Digita tu edad: '))
# formacion=int(input('''Cuál es su formación académica?
# 1. Pregrado (profesional)
# 2. Posgrado
# 3. Tecnico-tecnólogo
# Escoge una: '''))

# match formacion:
#     case 1:
#         if años>=25 and años<=35:
#             print('Apto para la vacante')
#         else:
#             print('No apto para la vacante')
#     case 2:
#         if años>=25 and años<=35:
#             print('Apto para la vacante')
#         else:
#             print('Apto para la vacante')
#     case 3:
#         print('No eres apto para la vacante')

######################################################################################################
paso1,paso2,paso3,paso4=False,False,False,False
familia=0
ciclo=0
total=''

while ciclo!=5:
    ciclo=int(input('''1. Ingresar cantidad familiares: 
2. Ingresar datos de los familiares: 
3. Mostrar los resultados: 
4. Acerca de 
5. Salir 
'''))
    match ciclo:
        case 1:
            familia=int(input('Digite el número de familiares: '))
            print('')
            paso1=True
        case 2:
            if paso1==True:
                for f in range(0,familia,1):
                    peso=float(input(f'Digite el peso del familiar n°{f+1}:  '))
                    estatura=float(input(f'Digite la estatura (en cm) del familiar n°{f+1}:  '))
                    estaturam=estatura/100
                    operacion=peso/estaturam**2
                    parentesco=(input('Digite el parentesco: '))
                    edad=int(input('Digite su edad: '))
                    if edad>=20:
                        print('')
                        if operacion<=18.5:
                            total+=(f'El IMC del familiar con parentesco {parentesco} y edad de {edad} es: {operacion} y está en un nivel de bajo peso.\n')
                        elif operacion>18.5 and operacion<=24.9:
                            total+=(f'El IMC del familiar con parentesco {parentesco} y edad de {edad} es: {operacion} y está en un nivel normal.\n')
                        elif operacion>=25.0 and operacion<=28.9:
                            total+=(f'El IMC del familiar con parentesco {parentesco} y edad de {edad} es: {operacion} y está en un nivel de sobrepeso.\n')
                        elif operacion>=29.0 and operacion<=34.9:
                            total+=(f'El IMC del familiar con parentesco {parentesco} y edad de {edad} es: {operacion} y está en un nivel Obeso I.\n')
                        elif operacion>=35.0:
                            total+=(f'El IMC del familiar con parentesco {parentesco} y edad de {edad} es: {operacion} y está en un nivel Obeso II.\n')
                    else:
                        print('No puedes obtener el IMC')
                        print('')
        case 3:
                print(total)
        case 4:
            print('Mariana ACero y Doncan Jimenez')
        case 5:
            print('Fin de la operación')