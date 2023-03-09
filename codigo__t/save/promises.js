// class Person {
// 	constructor(name, instagram) {
// 		this.name = name
// 		this.instagram = instagram
// 	}
// }

// const data =  [
// 	['Lucas Dalto', '@SoyDalto'],
// 	['Ricardo Rojas', '@Richard'],
// 	['Robertico', '@robert'],
// 	['Camila Nesa', '@milanesa']
// ]

// const people = []

// for (const i in data) {
// 	people[i] = new Person(data[i][0], data[i][1])
// }

// function getPerson(id, callback) {
// 	if (people[id] === undefined) {
// 		callback('No se ha encontrado la persona')
// 	} else {
// 		callback(null, people[id], id)
// 	}
// }

// getPerson(3, (err, person, id) => {
// 	if (err) {
// 		console.log(err)
// 	} else {
// 		console.log(person.name)
// 		getInstagram(id, (err, instagram) => {
// 			if (err) {
// 				console.log(err)
// 			} else {
// 				console.log(instagram)
// 			}
// 		})
// 	}
// })

// function getInstagram(id, callback) {
// 	if (people[id].instagram === undefined) {
// 		callback('No se ha encontrado el instagram')
// 	} else {
// 		callback(null, people[id].instagram)
// 	}
// }



class Person {
	constructor(name, instagram) {
		this.name = name
		this.instagram = instagram
	}
}

const data =  [
	['Lucas Dalto', '@SoyDalto'],
	['Ricardo Rojas', '@Richard'],
	['Robertico', '@robert'],
	['Camila Nesa',]
]

const people = []

for (const i in data) {
	people[i] = new Person(data[i][0], data[i][1])
}

function getPerson(id) {
	return new Promise((resolve, reject) => {
		if (people[id] === undefined) reject("Don't have found this person.")
		else resolve(people[id])
	});
}

function getInstagram(id) {
	return new Promise((resolve, reject) => {
		if (people[id].instagram === undefined) reject("Don't have found the instagram account.")
		else resolve(people[id].instagram)
	})
}

let id = 2
getPerson(id).then(person => {
	console.log(person.name)
	return getInstagram(id)
}).then(instagram => {
	console.log(instagram)
}).catch(e => {
	console.log(e)
})