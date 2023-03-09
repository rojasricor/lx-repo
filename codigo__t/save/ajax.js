'use strict'

let request

if (window.XMLHttpRequest) request = new XMLHttpRequest()
else request = new ActiveXObject('Microsoft.XMLHTTP')

request.addEventListener('load', e => {
	let response
	if (request.status === 200 || request.status === 201) response = request.response
	else response = "i'm sorry, the resource was not found"
	console.log(JSON.parse(response))
})

request.open('POST', 'https://reqres.in/api/users')

request.setRequestHeader('Content-type', 'application/json;charset=UTF8')

request.send(JSON.stringify({
	'nombre': 'dalto',
	'trabajo': 'edutuber'
}))
