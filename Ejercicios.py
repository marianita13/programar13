#Evaluar las siguientes expresiones
A=2
B=5
C=1
s1=int(3 * A -4 * B / A**2)
s2=int((((B + C) / 2 * A + 10) * 3 * B) - 6)

print(f' EL primer valor es: ' ,s1)
print(f' EL segundo valor es: ' ,s2)
print('')
#calcular la ganancia mensual de la inversión
c=float(input('2) Digite el valor de su capital '))
ganancia=int(c*0.012)

print('La ganancia mensual será: ',ganancia, 'pesos')
print('')
#calcular el área de un triángulo
Base=float(input('Digite el valor de la base '))
Altura=float(input('Digite el valor de la altura '))
Area=(Base*Altura)/2

print(f' EL área del triángulo es:', Area)
print('')
#calcular el salario de un vendedor de autos
salario=980000
Autos=int(input('4) Digite el numero de carros vendidos en el mes '))
monto=float(input('Digite el total del monto de ventas '))
porcentaje=(monto/Autos)*0.05
pago=(salario + (170000 * Autos) + (porcentaje * Autos))

print(f' el salario total es de ', pago, 'pesos')
print('')
#Hallar el promedio de las notas
Nota1=float(input('Digite la nota 1 '))
Nota2=float(input('Digite la nota 2 '))
Nota3=float(input('Digite la nota 3 '))
Nota4=float(input('Digite la nota 4 '))

p1=((Nota1+Nota2)/2)*0.4
p2=((Nota3+Nota4)/2)*0.6
total=(p1+p2)

print(f' el promedio de las notas es de ', total)
print('')
#Calcular el numero de pulsaciones
edad=int(input('Digite su edad '))
num_pulsaciones=(220-edad)/10

print(f' Usted debería tener', num_pulsaciones, 'por minuto')
print('')
#Calcular el sueldo completo
salario_base=float(input('Digite el valor de su salario '))
venta1=float(input('Digite el valor de la venta 1 '))
venta2=float(input('Digite el valor de la venta 2 '))
venta3=float(input('Digite el valor de la venta 3 '))

comision=((venta1+venta2+venta3)*0.1)
sueldo=(salario_base+comision)

print(f' EL sueldo total es de ', sueldo)
print('')
#Calificación general de 3 materias

#promedio materia matemáticas
evaluacionM=float(input('Digite la nota de su examen '))
evap=(evaluacionM*0.9)
tarea1M=float(input('Digite la nota de la tarea 1 '))
tarea2M=float(input('Digite la nota de la tarea 2 '))
tarea3M=float(input('Digite la nota de la tarea 3 '))
PromedioTM=((tarea1M+tarea2M+tarea3M)/3)*0.1
print('')
promedioM=(evap+PromedioTM)

print(f' el promedio de matemáticas es ', promedioM)

#promedio materia física
evaluacionF=float(input('Digite la nota de su examen '))
evapf=(evaluacionF*0.8)
tarea1F=float(input('Digite la nota de la tarea 1 '))
tarea2F=float(input('Digite la nota de la tarea 2 '))
promedioTF=((tarea1F+tarea2F)/2)*0.2
print('')
promedioF=(evapf+promedioTF)

print(f' el promedio de física es ', promedioF)

#promedio materia quimica
evaluacionQ=float(input('Digite la nota de su examen '))
evapq=(evaluacionQ*0.85)
tarea1q=float(input('Digite la nota de la tarea 1 '))
tarea2q=float(input('Digite la nota de la tarea 2 '))
tarea3q=float(input('Digite la nota de la tarea 3 '))
promedioTQ=((tarea1q+tarea2q+tarea3q)/3)*0.15
print('')
promedioQ=(evapq+promedioTQ)

print(f' el promedio de química es ', promedioQ)

promedio_total=(promedioQ+promedioM+promedioF)/3
print('')

print(f' el promedio de las 3 materias es ', promedio_total)