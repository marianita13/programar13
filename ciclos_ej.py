# equilatero=0
# isosceles=0
# escaleno=0

# for n in range (1,5):
#     L1,L2,L3=0,0,0
#     while L1 == 0:
#         L1=float(input('Digite uno de los lados del triángulo: '))
#     while L2 == 0:
#         L2=float(input('Digite uno de los lados del triángulo: '))
#     while L3 == 0:
#         L3=float(input('Digite uno de los lados del triángulo: '))
#     print('')
#     if L1==L2 and L1==L3 and L2==L3:
#         print('Es un triángulo escaleno.')
#         print('')
#         equilatero+=1
#     elif  (L1 == L2 and L1 != L3) or (L1 == L3 and L1 != L2) or (L2 == L3 and L2 != L1):
#         print('ES un tríangulo isósceles.')
#         print('')
#         isosceles+=1
#     elif L1 != L2 and L2 != L3 and L1 != L3:
#         print('Es un triángulo escaleno.')
#         print('')
#         escaleno+=1
# print(F'Hay {equilatero} triángulos equilateros')
# print(F'Hay {isosceles} triángulos isosceles')
# print(F'Hay {escaleno} triángulos escaleno.')
# print('')

# if equilatero<isosceles and equilatero<escaleno:
#     print(F'Hay una menor cantidad de {equilatero} triángulos equilateros')
# if (equilatero==isosceles) and (equilatero<escaleno):
#     print(f'Hay la misma cantidad {equilatero,isosceles} de triángulos equilateros e isosceles')
# if isosceles<equilatero and isosceles<escaleno:
#     print(f'Hay una menor cantidad de {isosceles} triángulos isosceles.')
# if (equilatero==escaleno) and (isosceles>escaleno):
#     print(f'Hay la misma cantidad {equilatero,escaleno} de triángulos equilateros y escalenos')
# if escaleno<isosceles and escaleno<equilatero:
#     print(f'Hay una menor cantidad de {escaleno} triángulos escalenos.')
# if (escaleno==isosceles) and (equilatero>escaleno):
#     print(f'Hay la misma cantidad {escaleno,isosceles} de triángulos equilateros e isosceles')

##########################################################################################################

# for n in range (5):
#     for t in range (5,n,-1):
#         print(t, end='')
#     print('')

# for n in range (5):
#     for t in range (5,n-1,-1):
#         print(t, end='')
#     print('')

########################################################################################################

# dividendo=int(input('Digite el dividendo: '))
# divisor=int(input('Digite el divisor: '))
# cociente=dividendo
# i = 0
# while cociente >= divisor:
#     cociente-=divisor
#     i+=1
# print(f'cociente es {i} y residuo es {dividendo-(divisor*i)}')

#######################################################################################################33

matriz=0
for a in range (1,11):
    print(a, end='  ',)
print('')
for b in range (11,21):
    print(b, end=' ')
print('')
for c in range (21,31):
    print(c, end=' ')
print('')
for d in range (31,41):
    print(d, end=' ')
print('')
for e in range (41,51):
    print(e, end=' ')
print('')

Bogota=[19,19,17,18,20]
Bucaramanga=[27,26,26,26,27]
Medellin=[27,26,26,27,29]
ciudades=[Bogota,Bucaramanga,Medellin]
nombres=('Bogota','Bucaramanga','Medellin')
cont=0

cont=0
for i in ciudades:
    maximo=max(i)
    print(f'La temperatura máxima de {nombres[cont]} es {maximo}')
    minimo=min(i)
    print(f'La temperatura mínima de {nombres[cont]} es {minimo}')
    prom=sum(i)/len(i)
    print(f'La temperatura promedio de {nombres[cont]} es: {prom}')
    print('')
    cont+=1