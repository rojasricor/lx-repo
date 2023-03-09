const materiasHTML = document.querySelector('.materias')

const materias = [
	{
		nombre: 'Fisica 4',
		nota: 7
	},
	{
		nombre: 'Calculo 4',
		nota: 8
	},
	{
		nombre: 'Bases de datos 3',
		nota: 3
	},
	{
		nombre: 'Integrales 4',
		nota: 6
	},
	{
		nombre: 'Programacion 4',
		nota: 10
	}
]

function obtenerMateria(id) {
	return new Promise((resolve, reject) => {
		const materia = materias[id]
		if (materia === undefined) reject('La materia no existe')
		else setTimeout(() => resolve(materia), Math.random() * 1000)
	})
}

const returnMaterias = async () => {
	let materia = []
	for (const i in materias) {
		materia[i] = await obtenerMateria(i)
		let newHTMLCode = `
		<div class="materia">
			<div class="nombre">${materia[i].nombre}</div>
			<div class="nota">${materia[i].nota}</div>
		</div>`
		materiasHTML.innerHTML += newHTMLCode
	}
}

returnMaterias()