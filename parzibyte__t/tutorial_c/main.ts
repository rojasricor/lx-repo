// Variables
let nombre: string = "Ricardo";
const numero: number = 42;
var age: number = 18;


// Funciones
function saludar(nombre: string, edad: number): string {
    return `Hola ${nombre} tu tienes ${edad} anios.`;
}

const saludo = saludar("Ricardo", 18);

// Clases


class Persona {

    nombre: string;
    edad: number;
    otherNumber: number;

    constructor(nombre: string, edad: number, number: number) {
        this.nombre = nombre;
        this.edad = edad;
        this.otherNumber = number;
    }

    sumar(): number {
        // @ts-check
        return this.edad + this.otherNumber;
    }
}

const persona = new Persona("Ricardo", 30, 23);
let suma = persona.sumar();

console.log(persona);
console.log(suma);
