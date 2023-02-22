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
const porcentajesGeneros=document.getElementById('porcentaje')

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
    let adultosMayores=personas.filter(el=>el.edad>=50).map(el=>el.nombre)
    let adultos=personas.filter(el=>el.edad>18 && el.edad<50).map(el=>el.nombre)
    let kids=personas.filter(el=>el.edad<18).map(el=>el.nombre)

    let contenido=''
    contenido+=`<table><th>Adultos Mayores</th><th>Adultos</th><th>Kids</th>`
    let total=[adultosMayores.length,adultos.length,kids.length]
    total=Math.max(...total)

    for(i=0;i<total;i++){
        let Tadultosmayores=''
        let Tadultos=''
        let Tkids=''
        if (adultosMayores[i]==null){
            Tadultosmayores=' '
        }else{
            Tadultosmayores=Tadultosmayores[i]
        }
        if (adultos[i]==null){
            Tadultos=' '
        }else{
            Tadultos=Tadultos[i]
        }
        if (kids[i]==null){
            Tkids=' '
        }else{
            Tkids=Tkids[i]
        }
        contenido+=`<tr><td>${Tadultosmayores}</td><td>${Tadultos}</td><td>${Tkids}</td></tr>`
    }
contenido+=`</table>`
document.getElementById('pantalla').innerHTML=contenido
}

porcentajesGeneros.addEventListener('click',()=>{
    let femenino=x
    let masculino=y
})