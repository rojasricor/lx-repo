const inputs = document.getElementById('inputs').children;
async function search() {
	const resultado = await fetch('http://localhost:3000/api/customers', {
		'method': 'GET',
		'headers': {
			'Content-Type': 'application/json'
		}
	});

	const request = await resultado.json();
	var row = '';
	request.forEach(item => {
		 row += `
		<tr>
			<td>${item[1]}</td>
			<td>${item[2]}</td>
			<td>${item[3]}</td>
			<td>${item[4]}</td>
			<td>
			<button onclick="remove(${item[0]});" class="button is-danger">Eliminar</button>
			<button onclick="edit(${item[0]});" class="button js-modal-trigger" data-target="modal-js-example">Editar</button>
			</td>
		</tr>`;
	});
	document.getElementById('customers').innerHTML = row;
}
search();

async function remove(id) {
	if (confirm('Estas seguro que deseas eliminarlo?')) {
		await fetch(`http://localhost:3000/api/customer/${id}`, {
			'method': 'DELETE',
			'headers': {
				'Content-Type': 'application/json'
			}
		});
	}
	search();
}

function clear() {
	inputs[0].value = '';
	inputs[1].value = '';
	inputs[2].value = '';
	inputs[3].value = '';
	inputs[4].value = '';
}

async function save() {
	clear();
	const inputs = document.getElementById('inputs').children;
	document.getElementById('save').onclick = async () => {
		const json = {
			'firstname': inputs[0].value,
			'lastname': inputs[1].value,
			'email': inputs[2].value,
			'phone': inputs[3].value,
			'address': inputs[4].value
		}

		const respose = await fetch(`http://localhost:3000/api/customer`, {
			'method': 'POST',
			'headers': {
				'Content-Type': 'application/json'
			},
			'body': JSON.stringify(json)
		});
		if (respose.ok) {
			closeAllModals();
			location.reload();
		}
	}
}

async function edit(id) {
	const resultado = await fetch(`http://localhost:3000/api/customer/${id}`, {
		'method': 'GET',
		'headers': {
			'Content-Type': 'application/json'
		}
	});

	const request = await resultado.json();
	openModal(document.getElementById('modal-js-example'));
	const data = request[0];
	inputs[0].value = data[1];
	inputs[1].value = data[2];
	inputs[2].value = data[3];
	inputs[3].value = data[4];
	inputs[4].value = data[5];
	document.getElementById('save').onclick = async () => {
		const json = {
			'id': data[0],
			'firstname': inputs[0].value,
			'lastname': inputs[1].value,
			'email': inputs[2].value,
			'phone': inputs[3].value,
			'address': inputs[4].value
		};

		const respose = await fetch(`http://localhost:3000/api/customer`, {
			'method': 'PUT',
			'headers': {
				'Content-Type': 'application/json'
			},
			'body': JSON.stringify(json)
		});
		if (respose.ok) {
			closeAllModals();
			location.reload();
		}
	}
}