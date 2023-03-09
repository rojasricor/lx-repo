const sendBtn = document.getElementById('snd-nota')

sendBtn.addEventListener('click', function sendNota(e) {
	let resultado, msg
	try {
		const prevRes = parseInt(document.getElementById('nota-alumno').value)
		if (isNaN(prevRes)) throw 'Noooo'
		resultado = verifyAprobation(8, 4, prevRes)
		msg       = defineMsg(resultado[1])
	} catch(e) {
		resultado = `${document.getElementById('nota-alumno').value} isn't a number`
		msg       = 'Error'
	}
	openModal(resultado[0], msg)
})

function defineMsg(prevRes) {
	switch(prevRes) {
		case 1:
			return "Don't you be as hijo de puta!"
			break
		case 2:
			return "You're very bad"
			break
		case 3:
			return "You're baaaaadd"
			break
		case 4:
			return "You're bad bad"
			break
		case 5:
			return "You're bad regular"
			break
		case 6:
			return "You're regular"
			break
		case 7:
			return "You're good"
			break
		case 8:
			return "You're very good"
			break
		case 9:
			return "Woow excelent!!!!"
			break
		case 10:
			return "You're insuperable woowow wwowow!!!"
			break
		default:
			return null
	}
}

function verifyAprobation(n1, n2, prevRes) {
	prom = (n1 + n2 + prevRes) / 3
	return prom >= 7
	? ['<span class="green">APROBADO</span>', Math.round(prom)]
	: ['<span class="red">DESAPROBADO</span>', Math.round(prom)]
}

function openModal(res, msg) {
	document.querySelector('.resultado').innerHTML = res
	document.querySelector('.mensaje').innerHTML   = `Tu prueba: ${msg}`
	const modal           = document.querySelector('.modal-background')
	modal.style.display   = 'flex'
	modal.style.animation = 'aparecer 1s forwards'
}