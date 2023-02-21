const personas=[
    {nombre:'Tasha', edad:21, genero:'f', fecha:{dia:01,mes:09,year:2002}},
    {nombre:'Tyrone', edad:19, genero:'m', fecha:{dia:01,mes:07,year:2004}},
    {nombre:'Uniqua', edad:60, genero:'f', fecha:{dia:01,mes:04,year:1963}},
    {nombre:'Austin', edad:13, genero:'m', fecha:{dia:01,mes:01,year:2009}},
    {nombre:'Pablo', edad:09, genero:'m', fecha:{dia:01,mes:06,year:2014}}]

const nombre=document.getElementById('nombre')
const edad=document.getElementById('edad')
const genero=document.getElementById('genero')
const fecha=document.getElementById('fecha')

const insertar=document.getElementById('insert')
const mostrarNombres=document.getElementById('mNombres')
const mostrarEdades=document.getElementById('mEdades')

insertar.addEventListener('click',()=>{
    let name=nombre.value
    let age=edad.value
    let gender=genero.value
    let date=fecha.value
    if (name=='' || age=='' || gender=='' || date==''){
        alert('Existen campos vacios')
    }else{
    date=date.split('-')
    let day=Number(date[2])
    let month=Number(date[1])
    let year=Number(date[0])
    personas.push({nombre:name, edad:age, genero:gender, 
        fecha:{day:day, month:month, year:year}})
    nombre.value=''
    edad.value=''
    genero.value=''
    fecha.value=''
    }
})

mostrarNombres.addEventListener('click',function(){
    let contenido=''
    contenido=`<table><th>Nombres</th>`
    let nombres=personas.map(x=>x.nombre)
    nombres.forEach(nombre=>{
        contenido+=`<tr><td>${nombre}</td></tr>`
    })
    contenido+=`</table>`
    document.getElementById('pantalla').innerHTML=contenido
})

mostrarEdades.addEventListener('click',ages)
function ages(){
    let adultosmayores=personas.filter(e=> e.edad>=50).map(el => el.nombre)
    let adultos=personas.filter(e=> e.edad>=18 && e.edad<50).map(el => el.nombre)
    let niños=personas.filter(e=> e.edad<18).map(el => el.nombre)

    let contenido=`Adultos mayores<br>`
    adultosmayores.forEach(nombre=>{
        contenido+=`${nombre}<br>`
    })
    contenido+=`<br>Adultos<br>`
    adultos.forEach(nombre=>{
        contenido+=`${nombre}<br>`
    })
    contenido+=`<br>Niños<br>`
    niños.forEach(nombre=>{
        contenido+=`${nombre}<br>`
    })
    document.getElementById('pantalla').innerHTML=contenido
}