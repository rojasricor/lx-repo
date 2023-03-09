const alumnos = [
	{
		nombre: 'Lucas Dalto',
		email: 'SoyDalto@gmail.com',
		materia: 'Fisica 3'
	},
	{
		nombre: 'Karin Guerra',
		email: 'karin@gmail.com',
		materia: 'Fisica 1'
	},
	{
		nombre: 'George Ramirez',
		email: 'gramirez@gmail.com',
		materia: 'Ingles'
	},
	{
		nombre: 'Facundo Roberto',
		email: 'robert@gmail.com',
		materia: 'Calculo 2'
	},
	{
		nombre: 'Cofla XD',
		email: 'coflaxd@gmail.com',
		materia: 'Literatura'
	},
	{
		nombre: 'Natalia',
		email: 'na@gmail.com',
		materia: 'Ciencias de la computacion'
	},
	{
		nombre: 'Kimberly reyes',
		email: 'KyReyes@gmail.com',
		materia: 'Estructuras de informacion'
	}
]

const btn       = document.querySelector('.btn-confirmar'),
	  container = document.querySelector('.grid-container')

alumnos.forEach(alumno => {
	container.innerHTML +=`
		<div class="grid-item nombre">${alumno.nombre}</div>
		<div class="grid-item email">${alumno.email}</div>
		<div class="grid-item materia">${alumno.materia}</div>
		<div class="grid-item semana">
			<select class="semana-elegida">
				<option value="Semana 1">Semana 1</option>
				<option value="Semana 2">Semana 2</option>
			</select>
		</div>`
})

btn.addEventListener('click', function confirmarSemana(e) {
	if (!confirm('Realmente quieres confirmar guardar?'))
		return
	let elementos = document.querySelectorAll('.semana')
	let semanaElegida = document.querySelectorAll('.semana-elegida')
	for (const elemento in elementos) {
		semana = elementos[elemento]
		semana.innerHTML = semanaElegida[elemento].value
	}
	document.body.removeChild(btn)
})
