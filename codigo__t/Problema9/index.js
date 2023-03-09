const form = {
    nombre:document.getElementById('nombre'),
    email:document.getElementById('email'),
    materia:document.getElementById('materia'),
    btnEnviar:document.getElementById('btn-enviar'),
    resultado:document.querySelector('.resultado')
}

form.btnEnviar.addEventListener('click', e => {
	e.preventDefault()
	let error = validarCampos()
	if (error[0]) {
		form.resultado.textContent = error[1]
		form.resultado.classList.add('danger')
	} else {
		form.resultado.textContent = 'Solicitud enviada correctamente'
		form.resultado.classList.add('success')
		form.resultado.classList.emove('danger')
	}
})

function validarCampos() {
	let error = []
	if (form.nombre.value.length < 5 || form.nombre.value.length > 40) {
		error[0] = true
		error[1] = 'El nombre es invalido'
		return error;
	} else if (form.email.value.length < 5
		|| form.email.value.length > 40
		|| form.email.value.indexOf('@') == -1
		|| form.email.value.indexOf('.') == -1) {
		error[0] = true
		error[1] = 'El email es invalido'
		return error;
	} else if (form.materia.value.length < 4 || form.materia.value.length > 40) {
		error[0] = true
		error[1] = 'La materia no existe'
		return error;
	}

	error[0] = false
	return error;
}
