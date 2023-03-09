// Variables
var nombre = "Ricardo";
var numero = 42;
var age = 18;
// Funciones
function saludar(nombre, edad) {
    return "Hola ".concat(nombre, " tu tienes ").concat(edad, " anios.");
}
var saludo = saludar("Ricardo", 18);
// Clases
var Persona = /** @class */ (function () {
    function Persona(nombre, edad, number) {
        this.nombre = nombre;
        this.edad = edad;
        this.otherNumber = number;
    }
    Persona.prototype.sumar = function () {
        // @ts-check
        return this.edad + this.otherNumber;
    };
    return Persona;
}());
var persona = new Persona("Ricardo", 30, 23);
var suma = persona.sumar();
console.log(persona);
console.log(suma);
