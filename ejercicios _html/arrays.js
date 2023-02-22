/* Ejercicio 1 */

// const animales=['jirafa','venado','gato','elefante','lobo','pajaro','perro','oso','ballena','puercoespin']
// let opciones=0

// while (opciones != 5){
//     opciones=+prompt(`
//     1. Agregar animales
//     2. Ordenarlos alfabeticamente
//     3. Animales dentro de la lista
//     4. Saber si un animal está en la lista
//     5. Salir
//     Digite una opcion: `)
//     switch(opciones){
//         case 1:
//             for (i=0; i<20; i++){
//                 let animal=prompt('Digite el animal: ')
//                 animales.push(animal)
//             }break;
//         case 2:
//             let contenido=animales.sort()
//             console.log(contenido)
//             break;
//         case 3:
//             let numero=+prompt('Digite un número del 1 al 10: ')
//             let orden=animales.slice(numero)
//             console.log(orden)
//             break;
//         case 4:
//             let pets=prompt('Digite el animal: ').toLowerCase()
//             let contener=animales.includes(pets)
//             if (contener==true){
//                 console.log('El animal si está')
//             }else{
//                 console.log('El animal no se encuentra');
//             }break;
//         case 5:
//             console.log('Hasta luego')
//             break;
//         default:
//             ('Número no dentro del menú')
// }}


/* Ejercicio 2 */

// let arreglo=[1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2]
// let repetidos=[]
// let contador=[]

// let numero=+prompt('Digite el número a buscar: ')

// if (arreglo.includes(numero)){
//     let posicion=arreglo.indexOf(numero)
//     let Uposicion=arreglo.lastIndexOf(numero)
//     console.log(`El número se encuentra en la posición ${posicion} y en la posición ${Uposicion}`)
// }else{
//     console.log('EL número no se encuentra en el arreglo.')
// }


/* Ejercicio 3 */

// let arreglo=[1,0,4,8,5,7,6,8]

// let numero=+prompt('Digite el número que desea añadir:')
// let posicion=+prompt('Digite la posición del nuevo número: ')

// arreglo.splice(posicion,0,numero);

// console.log(arreglo)


/* Ejercicio 4 */

// let nombres=[]

// let cantidad=+prompt('Digite la cantidad de nombres a ingresar')
// for (i=0; i<cantidad; i++){
//     let nombre=prompt('Digite el nombre')
//     nombres.push(nombre)
// }
// console.log(nombres)
// let alfabeto=nombres.sort()
// console.log(alfabeto);


/* Ejercicio 5 */

