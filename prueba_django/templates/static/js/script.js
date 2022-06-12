document.addEventListener("DOMContentLoaded", search);
const URL_API = 'http://localhost:8000/'
//Variable para manejar los datos de clientes.
var clientes_aux = []

function iniciar() {
    search()
}
function agregar() {
    clean()
    abrirformulario()
}
function abrirformulario() {
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class", "modaled opened");
}
function abrirmodificar() {
    htmlModal = document.getElementById("modificar");
    htmlModal.setAttribute("class", "modaled opened");
}
function cerrarModal_mod() {
    htmlModal = document.getElementById("modificar");
    htmlModal.setAttribute("class", "modaled");
}
function cerrarModal() {
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class", "modaled");
}
function abrirpedido() {
    htmlModal = document.getElementById("pedido");
    htmlModal.setAttribute("class", "modaled opened");
}

function cerrarModal_ped() {
    htmlModal = document.getElementById("pedido");
    htmlModal.setAttribute("class", "modaled");
}

function botonpendiente() {
    alert("El pedido está pendiente.")
}

async function search() {
    var url = URL_API + 'clientes'
    var respuesta = await fetch(url, {
        "method": 'GET',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    clientes_aux = await respuesta.json();
    var html = ''

    for (cliente of clientes_aux) {
        var fila = `<tr>
        <td>${cliente.id} </td>
        <td>${cliente.nombre} </td>
        <td>${cliente.apellido} </td>
        <td>${cliente.telefono} </td>
        <td>${cliente.email} </td>
        <td>
            <button class="button button3">Pendiente</button>
            <button class="button button2">En proceso</button>
            <button onclick="botonpendiente()" class="button button1">Listo</button>
        </td>
        <td>
            <button class="button buttonEditar" onclick="editar(${cliente.id})">Editar</button>
            <button class="button buttonBorrar" onclick="remove(${cliente.id})" >Borrar</button>
            <button class="button buttonArchivar" onclick="">Archivar</button>
        </td>
        </tr>`
        html = html + fila;
    }
    document.querySelector('#customers > tbody').outerHTML = html;
}

function editar(id) {
    abrirmodificar()
    var cliente_auxiliar = clientes_aux.find(x => x.id == id)
    console.log(cliente_auxiliar)
    document.getElementById('modal_mod_id').value = cliente_auxiliar.id
    document.getElementById('modal_mod_apellido').value = cliente_auxiliar.apellido
    document.getElementById('modal_mod_mail').value = cliente_auxiliar.mail
    document.getElementById('modal_mod_nombre').value = cliente_auxiliar.nombre
    document.getElementById('modal_mod_telefono').value = cliente_auxiliar.telefono
}

async function modifi() {
    ///Creamos el JSON para mandar a la base de datos.
    var data = {
        "id": document.getElementById('modal_mod_id').value,
        "apellido": document.getElementById('modal_mod_apellido').value,
        "mail": document.getElementById('modal_mod_mail').value,
        "nombre": document.getElementById('modal_mod_nombre').value,
        "telefono": document.getElementById('modal_mod_telefono').value
    }


    var url = URL_API + 'clientes'
    await fetch(url, {
        "method": 'PUT',
        "body": JSON.stringify(data),
        "headers": {
            "Content-Type": 'application/json'
        }
    })

    window.location.reload()
}

async function remove(id) {
    respuesta = confirm('Estás seguro que lo vas a borrar?')
    if (respuesta) {
        var url = URL_API + 'clientes/' + id
        await fetch(url, {
            "method": 'DELETE',
            "headers": {
                "Content-Type": 'application/json'
            }
        })
    }
    window.location.reload()
}

function clean() {
    document.getElementById('modal_apellido').value = ''
    document.getElementById('modal_dni').value = ''
    document.getElementById('modal_mail').value = ''
    document.getElementById('modal_nombre').value = ''
    document.getElementById('modal_telefono').value = ''
}


async function save() {
    ///Creamos el JSON para mandar a la base de datos.
    var data = {
        "id": document.getElementById('modal_dni').value,
        "apellido": document.getElementById('modal_apellido').value,
        "mail": document.getElementById('modal_mail').value,
        "nombre": document.getElementById('modal_nombre').value,
        "telefono": document.getElementById('modal_telefono').value
    }


    var url = URL_API + 'clientes'
    await fetch(url, {
        "method": 'POST',
        "body": JSON.stringify(data),
        "headers": {
            "Content-Type": 'application/json'
        }
    })

    window.location.reload()
}

