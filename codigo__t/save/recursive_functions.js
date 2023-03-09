'use strict';

(function validateAge(msg) {
	let age
	try {
		age = msg ? prompt(msg) : prompt("Enter your age")
		age = parseInt(age)
		if (isNaN(age)) throw "Enter a number for your age"
		console.log(age > 18 ? "You're an a adult" : "You aren't a adult")
	} catch(e) {
		validateAge(e)
	}
})()