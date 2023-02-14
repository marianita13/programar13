// /* Ejercicio 1*/
// let num1=parseInt(prompt('Digite un número: '))
// let num2=parseInt(prompt('Digite un número: '))
// let num3=parseInt(prompt('Digite un número: '))

// if (num1==num2 || num1==num3 || num2==num3){
// console.log('Los números no pueden ser iguales')
// }else{
// let maximo=(Math.max(num1,num2,num3))
// let minimo=(Math.min(num1,num2,num3))
// console.log('El número mayor es:',maximo)
// console.log('El número menor es:',minimo)
// }


// /*Ejercicio 2*/
// let base=parseInt(prompt('Digite la base del tríangulo en cm: '))
// let altura=parseInt(prompt('Digite la altura del tríangulo en cm: '))
// var area=(base*altura)/2
// var otro=(base*2)+10

// if (base == altura){
// console.log('Los datos no pueden ser iguales')
// }else if (base>=5 && altura >=4){
// console.log('El área del tríangulo es:', area)
// }else{
// console.log('El área es:',otro)
// }


// /*Ejercicio 3*/
// var numero=parseInt(prompt('Digite un número: '))

// if (numero%2==0){
//   console.log('El número es par')
// }else{
//   console.log('El número es impar')
// }


// /*Ejercicio 5*/
// var num=parseInt(prompt('Digita un número del 1 al 20: '))

// if (num==19 || num==20){
// console.log('Tu nota es: A')
// }else if(num>=16 && num<=18){
// console.log('Tu nota es: B')
// }else if(num>=13 && num<=15){
// console.log('Tu nota es: C')
// }else if(num>=10 && num<=12){
// console.log('Tu nota es: D')
// }else if(num>=1 && num<=9){
// console.log('Tu nota es: E')
// }

// /*Ejercicio 6*/
// var numero1=parseInt(prompt('Digita el primer número: '))
// var numero2=parseInt(prompt('Digita el segundo número: '))

// if (numero1%numero2==0 || numero2%numero1==0){
// console.log('Si son múltiplos')
// }else{
// console.log('No son múltiplos')
// }


// /*Ejercicio 7*/
// var numero=parseInt(prompt('Digita un número: '))

// if (numero<0){
// console.log('El número es negativo')
// }else if (numero==0){
// console.log('El número es igual a 0')
// }else{
// console.log('El número es positivo')
// }


// /*Ejercicio 8*/
// var numero1=parseInt(prompt('Digite un número entero: '))
// var numero2=parseInt(prompt('Digite un número entero: '))
// var numero3=parseInt(prompt('Digite un número entero: '))
// let promedio=(numero1+numero2+numero3)/3

// promedio>=5 ? console.log('True'):console.log('False')


// /*Ejercicio 9*/
// let numerito=parseInt(prompt('Digita un número entero positivo: '))

// if (numerito<=0){
// console.log('El número debe ser positivo')
// }else{
// numerito%2==0 ? console.log('El número es par'): console.log('El número es impar')
// }


// /*Ejercicio 10*/
// let diametro=parseFloat(prompt('Digite el díametro de la reuda: '))
// let grosor=parseFloat(prompt('Digite el grososr de la rueda: '))

// if (diametro>1.4){
// console.log('la rueda es para un vehículo grande')
// }else if (diametro<=1.4 && diametro>0.8){
// console.log('La rueda es para un vehículo mediano')
// }else{
// console.log('La rueda es para un vehículo pequeño')
// }

// if (diametro>1.4 && grosor<0.4 || diametro<=1.4 && diametro>0.8 && grosor<0.25){
// console.log('El grosor para esta rueda es inferior al recomendado')
// }


// let minutos=prompt('Digite el tiempo de duración de la llamada en min: ')

// let tipo=+prompt(`1. Local
// 2. Regional
// 3. Larga distancia Nacional
// 4. Larga distancia Internacional
// 5. Celular
// Digite una opción:`)

// switch(tipo){
//   case 1:
//     console.log(`El valor de la llamada es: ${minutos*50} pesos`)
//     break
//   case 2:
//     if (minutos>=5){
//       let descuento1=(minutos*100)*0.05
//     console.log(`El valor de la llamada es: ${(minutos*100)-descuento1} pesos`)
//     }else{
//     console.log(`El valor de la llamada es: ${minutos*100} pesos`)
//     }
//     break
//   case 3:
//     if (minutos>=5){
//       let descuento2=(minutos*100)*0.05
//     console.log(`El valor de la llamada es: ${(minutos*500)-descuento2} pesos`)
//     }else{
//       console.log(`El valor de la llamada es: ${minutos*500} pesos`)
//     }
//     break
//   case 4:
//     console.log(`El valor de la llamada es: ${minutos*700} pesos`)
//     break
//   case 5:
//     console.log(`El valor de la llamada es: ${minutos*200} pesos`)
//     break
//   default:
//     console.log('Digite eso bien')
// }


// let parcial1=+prompt('Digite la nota del parcial N°1: ')
// let parcial2=+prompt('Digite la nota del parcial N°2: ')

// let promediop=(parcial1*0.3)+(parcial2*0.3)

// if (parcial1<0 || parcial1>5 && parcial2<0 || parcial2>5){
//   console.log('Existen notas fuera del rango.')
// }else{
//   if (promediop<2.0){
//   console.log(`El estudiante no puede presentar el exámen final
//   Pierde la materia por bajo promedio y su nota definitiva es ${promediop}`)
//   }else{
//     let examenf=+prompt('Digite la nota del exámen final: ')
//     if (examenf<0 || examenf>5){
//     console.log('La nota está fuera del rango')
//     }else{
//       if (examenf<2.0){
//       console.log(`El estudiante reprobó el exámen final y su definitiva es de: ${examenf}`)
//       }else{
//         let promedio=(parcial1*0.3)+(parcial2*0.3)+(examenf*0.4)
//         if (promedio>=3.0){
//           console.log(`El estudiante aprueba la materia con una nota de ${promedio}`)
//         }else{
//           if (examenf>=2.0){
//             let habilitacion=+prompt('Digite la nota de la habilitación: ')
//             console.log(`La nota definitiva es de ${habilitacion}`)
//           }else{
//             console.log(`Reprueba la materia con una nota de ${promedio}`)
//           }
//         }
//       }
//     }
//   }
// }

//////////////////////////////////////////////////////////////////////////////////////////////////////

// for (let x=1;x<=10;x++)
//   console.log(x)

// let x=0

// while(x<=10){
//   console.log(x+1)
//   x+=1
// }

// let x=1
// do{
//   console.log(x)
//   x++
// }while (x<=10)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

// for (let x=0;x<=25;x++)
//   console.log(x*11)

// let x=0

// while(x<=500){
//   console.log(x)
//   x+=8
// }

//////////////////////////////////////////////////////////////////////////////////////////////

// let num1=+prompt('Digite el primer número: ')
// let num2=+prompt('Digite el segundo número: ')

// if (num1>num2){
//   for (a=num2;a<=num1;a++){
//   if (a%2==0){
//   console.log(a)}
//   }
// }else if (num2>num1){
//   for (a=num1;a<=num2;a++){
//   if (a%2==0){
//   console.log(a)}
//   }
// }else if(num1==num2){
//   console.log('Los números son iguales')
// }

////////////////////////////////////////////////////////////////////////////////////////////////////

// let numeros=0
// let suma=0

// while(numeros!=9999){
//   suma+=numeros
//   numeros=+prompt('Digite los números que desea sumar: ')
// }
// console.log(suma)

///////////////////////////////////////////////////////////////////////////////////////////////////

// let numeros=[]
// let numero=1
// let suma=0
// let contador=0

// while (numero!=0){
//   numero=+prompt('Digita el número: ')
//   if (numero!=0){
//     numeros.push(numero)
//     suma+=numero
//     contador+=1
// }
// }
// let maximo=(Math.max.apply(null,numeros))
// let minimo=(Math.min.apply(null,numeros))
// let media=(suma/contador)
// console.log(`EL número mayor es ${maximo}.
// El número menor es: ${minimo}.
// La media es: ${media}`)

////////////////////////////////////////////////////////////////////////////////////////////////////

// for (i=1;i<=100;i++){
//   if (i%2==0 && i%3==0){
//     console.log(i)
//   }
// } 

////////////////////////////////////////////////////////////////////7

